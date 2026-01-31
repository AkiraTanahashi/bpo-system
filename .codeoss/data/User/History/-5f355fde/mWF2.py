from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from core import views
from django.conf.urls.i18n import i18n_patterns 

urlpatterns = [path('', views.menu_view, name='menu'),]

# 言語コード（/en/ や /ja/）をつけたいURLをここに入れます
urlpatterns += i18n_patterns(
    path('api/', include('clients.urls')),
    path('admin/', admin.site.urls),
    # accountsなどの他のアプリもここに入れてOKです
    path('accounts/', include('django.contrib.auth.urls')),
    path('<str:customer_id>/', views.detail, name='detail'),
     path('', include('frontend.urls')),
)