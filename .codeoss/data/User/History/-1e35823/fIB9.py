from django.shortcuts import render
from django.http import HttpResponse
# ↓ これを追加（鍵機能）
from django.contrib.auth.decorators import login_required
from google.cloud import firestore
import datetime

# （Firestoreの設定などはそのまま）
db = firestore.Client(project='project-f577b35b-633d-4af8-904') # IDはあなたのもの

# ↓ @login_required をつけると、ログイン必須になります
@login_required
def index(request):
    # ... (中身は同じ) ...
    docs = db.collection('customers').stream()
    # ...
    return render(request, 'core/list.html', {'customers': customer_list})

@login_required
def detail(request, customer_id):
    # ... (中身は同じ) ...
    return render(request, 'core/detail.html', {'customer': customer_data})

# テスト用URLは、あえてログインなしでもOKにするか、ここも守るかは自由です
def test_firestore(request):
    # ...
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