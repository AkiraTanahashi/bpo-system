from django.shortcuts import render # ← 追加
from django.http import HttpResponse
from google.cloud import firestore
import datetime

# プロジェクトID設定（そのままでOK）
db = firestore.Client(project='project-f577b35b-633d-4af8-904')

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

def test_firestore(request):
    # （ここは変更なし。データ追加用として残します）
    doc_ref = db.collection('customers').document()
    doc_ref.set({
        'name': '追加テスト次郎', # 名前を少し変えてみます
        'status': '商談中',
        'timestamp': datetime.datetime.now(),
        'memo': 'リスト表示のテスト用データです'
    })
    # 追加したらトップページに戻るようにする
    return HttpResponse(f"<script>alert('追加しました！'); window.location.href='/';</script>")