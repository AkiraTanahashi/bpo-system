from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

# 国際化対応（/ja/ や /en/）のパターン設定
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    
    # APIの窓口
    path('api/', include('clients.urls')),
    
    # ログイン・ログアウト機能
    path('accounts/', include('django.contrib.auth.urls')),
    
    # ★ここが重要：トップページ（''）は frontendアプリ に任せる
    path('', include('frontend.urls')),
)