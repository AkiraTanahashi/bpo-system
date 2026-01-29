from django.http import HttpResponse
from google.cloud import firestore
import datetime

# Firestoreクライアントの初期化
# Cloud RunやCloud Shellでは、自動で認証情報を読み取るためキーファイルは不要です
db = firestore.Client(project='project-f577b35b-633d-4af8-904')

def index(request):
    return HttpResponse("<h1>IKIGAI System 起動中...</h1><p>URLの末尾に /test をつけるとFirestoreテストを行います。</p>")

def test_firestore(request):
    # テストデータをFirestoreに保存
    doc_ref = db.collection('customers').document()
    doc_ref.set({
        'name': 'テスト太郎',
        'status': '新規',
        'timestamp': datetime.datetime.now(),
        'memo': 'Djangoからの書き込みテストです'
    })
    
    return HttpResponse(f"<h2>✅ 保存成功！</h2><p>ID: {doc_ref.id} でFirestoreに保存しました。</p>")