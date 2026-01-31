from django.urls import path
from . import views

urlpatterns = [
    # トップページ（''）に来たら、views.py の menu_view を呼び出す
    path('', views.menu_view, name='menu'),
    path('calendar/', views.calendar_view, name='calendar'),
]