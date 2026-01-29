from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from google.cloud import firestore
import requests

db = firestore.Client(project='project-f577b35b-633d-4af8-904')

@login_required
def index(request):
    # --- ① WordPress連携（安全装置付き） ---
    wp_news = cache.get('wp_news_cache')

    if not wp_news:
        wp_news = [] # 初期値は「空っぽ」にしておく
        
        # ★ここに「本当の」WordPressのURLを入れてください
        # もし無いなら、このURLのままにしておけば、下の except に流れて無視されます
        target_url = "https://your-wordpress-site.com/wp-json/wp/v2/posts?per_page=3"
        
        # URLがダミーのままかチェック（これがループ防止の鍵！）
        if "your-wordpress-site.com" not in target_url:
            try:
                # timeout=1 に設定。1秒で返事がなければ即切り捨てます
                response = requests.get(target_url, timeout=1)
                
                if response.status_code == 200:
                    posts = response.json()
                    for post in posts:
                        wp_news.append({
                            'title': post['title']['rendered'],
                            'link': post['link'],
                            'date': post['date'][:10]
                        })
                    # 成功したときだけキャッシュする
                    cache.set('wp_news_cache', wp_news, 3600)
            except Exception as e:
                # タイムアウトやエラーが起きても、何もせずスルーする
                # print(f"WP取得エラー: {e}") # ログを見たい場合はコメントアウトを外す
                pass

    # --- ② Firestoreから顧客データを取得 ---
    # ここは止まらないはずです
    docs = db.collection('customers').stream()
    customer_list = []
    for doc in docs:
        data = doc.to_dict()
        data['id'] = doc.id
        customer_list.append(data)
    
    context = {
        'customers': customer_list,
        'news': wp_news
    }
    return render(request, 'core/list.html', context)