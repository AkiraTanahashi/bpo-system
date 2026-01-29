from django.contrib import admin
from django.urls import path, include # includeを追加
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # ↓ これを追加！ログイン機能一式が入ります
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 既存のURL
    path('', views.index, name='index'),
    path('test/', views.test_firestore),
    path('<str:customer_id>/', views.detail, name='detail'),
]
