from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    # パスの部分を空っぽ '' にすることで、ここがトップページになります
    # name='menu' とすることで、ログイン後にここへ自動で飛んできます
    path('', views.menu_view, name='menu'),
]
# ログイン必須にする（セキュリティ対策）
@login_required
def menu_view(request):
    # ユーザー名を渡してあげる
    context = {
        'username': request.user.username
    }
    return render(request, 'frontend/menu.html', context)