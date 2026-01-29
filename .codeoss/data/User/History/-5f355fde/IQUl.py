# mysite/urls.py (プロジェクト名のフォルダ内)

from django.contrib import admin
from django.urls import path, include  # includeを追加

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 以下の1行を追加します
    # これだけで ログイン、ログアウト、パスワード変更などのURLが有効になります
    path('accounts/', include('django.contrib.auth.urls')), 
]