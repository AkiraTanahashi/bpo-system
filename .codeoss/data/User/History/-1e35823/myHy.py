from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.conf import settings # ← 追加：settings.pyの中身を読むための道具
from google.cloud import firestore
import requests

db = firestore.Client(project='project-f577b35b-633d-4af8-904')

@login_required
def index(request):
    # --- ① WordPress連携（設定ファイル利用版） ---
    wp_news = cache.get('wp_news_cache')

    if not wp_news:
        wp_news = []
        
        # settings.py からURLを取得
        # getattrを使うと、もし設定し忘れていてもエラーにならず None が返るので安全です
        target_url = getattr(settings, 'WORDPRESS_API_URL', None)

        # URLが設定されていて、かつダミーではない場合のみ実行
        if target_url and "your-wordpress-site.com" not in target_url:
            try:
                # タイムアウトを1秒に設定（フリーズ防止）
                response = requests.get(target_url, timeout=1)
                
                if response.status_code == 200:
                    posts = response.json()
                    for post in posts:
                        wp_news.append({
                            'title': post['title']['rendered'],
                            'link': post['link'],
                            'date': post['date'][:10]
                        })
                    # 成功したら60分キャッシュ
                    cache.set('wp_news_cache', wp_news, 3600)
            except Exception:
                # 失敗しても無視
                pass

    # --- ② Firestore連携 ---
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