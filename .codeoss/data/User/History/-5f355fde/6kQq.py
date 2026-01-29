from django.contrib import admin
from django.urls import path
from core import views  # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),             # トップページ
    path('test/', views.test_firestore), # テスト用URL
]