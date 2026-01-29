from django.contrib import admin
from django.urls import path, include # includeを追加
from django.views.generic import TemplateView
from core import views
from django.conf.urls.i18n import i18n_patterns 

# まず、言語に関係ないURL（もしあれば）をここに書きます
urlpatterns = [
    # 今回は特にないので空でもOK
]

# 言語コード（/en/ や /ja/）をつけたいURLをここに入れます
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    # accountsなどの他のアプリもここに入れてOKです
    path('accounts/', include('django.contrib.auth.urls')),
        path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('test/', views.test_firestore),
    path('<str:customer_id>/', views.detail, name='detail'),
)

