from django.shortcuts import render
from django.http import HttpResponse
# 鍵機能の読み込み
from django.contrib.auth.decorators import login_required
from google.cloud import firestore
import datetime

# Firestore設定
db = firestore.Client(project='project-f577b35b-633d-4af8-904')

# ▼▼ ここが修正ポイント！鍵(@login_required)をつけて、中身も書きます ▼▼
@login_required
def index(request):
    # Firestoreから全データを取得
    docs = db.collection('customers').stream()
    
    # データを使いやすい形（リスト）に変換
    customer_list = []
    for doc in docs:
        data = doc.to_dict()
        data['id'] = doc.id # IDも一緒に持たせる
        customer_list.append(data)
    
    # HTMLにデータを渡して表示
    return render(request, 'core/list.html', {'customers': customer_list})
# ▲▲ 修正ここまで ▲▲

@login_required
def detail(request, customer_id):
    # IDを使ってFirestoreから1件だけ取得
    doc_ref = db.collection('customers').document(customer_id)
    doc = doc_ref.get()

    if doc.exists:
        customer_data = doc.to_dict()
        customer_data['id'] = doc.id
        return render(request, 'core/detail.html', {'customer': customer_data})
    else:
        return HttpResponse("エラー: その顧客は見つかりませんでした。")

# テスト用（ログインなしでもOKにしておきますが、必要なら @login_required をつけてください）
def test_firestore(request):
    doc_ref = db.collection('customers').document()
    doc_ref.set({
        'name': '追加テスト次郎',
        'status': '商談中',
        'timestamp': datetime.datetime.now(),
        'memo': 'リスト表示のテスト用データです'
    })
    return HttpResponse(f"<script>alert('追加しました！'); window.location.href='/';</script>")