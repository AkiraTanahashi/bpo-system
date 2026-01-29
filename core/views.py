from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.conf import settings
from google.cloud import firestore
import requests
import datetime

# Firestore設定
db = firestore.Client(project='project-f577b35b-633d-4af8-904')

@login_required
def index(request):
    # --- ① WordPress連携（本番モード） ---
    # まずキャッシュ（メモリ）を確認
    wp_news = cache.get('wp_news_cache')

    if not wp_news:
        wp_news = []
        target_url = getattr(settings, 'WORDPRESS_API_URL', None)

        if target_url:
            try:
                # 2秒待っても返事がなければ、潔く諦めて画面を表示する（フリーズ防止）
                response = requests.get(target_url, timeout=2)
                
                if response.status_code == 200:
                    posts = response.json()
                    for post in posts:
                        wp_news.append({
                            'title': post['title']['rendered'],
                            'link': post['link'],
                            'date': post['date'][:10]
                        })
                    # 成功したら60分間保存
                    cache.set('wp_news_cache', wp_news, 3600)
            except Exception:
                # 通信エラー時は何もしない（空のリストのまま進む）
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

@login_required
def detail(request, customer_id):
    doc_ref = db.collection('customers').document(customer_id)
    doc = doc_ref.get()

    if doc.exists:
        customer_data = doc.to_dict()
        customer_data['id'] = doc.id
        return render(request, 'core/detail.html', {'customer': customer_data})
    else:
        return HttpResponse("エラー: その顧客は見つかりませんでした。")

def test_firestore(request):
    doc_ref = db.collection('customers').document()
    doc_ref.set({
        'name': '追加テスト次郎',
        'status': '商談中',
        'timestamp': datetime.datetime.now(),
        'memo': 'リスト表示のテスト用データです'
    })
    return HttpResponse(f"<script>alert('追加しました！'); window.location.href='/';</script>")