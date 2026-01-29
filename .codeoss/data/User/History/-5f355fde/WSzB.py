from django.contrib import admin
from django.urls import path
from core import views  # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')), # coreのURLを分離して管理しやすくします（後述）
]