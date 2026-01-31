from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# ログイン必須にする（セキュリティ対策）
@login_required
def menu_view(request):
    # ユーザー名を渡してあげる
    context = {
        'username': request.user.username
    }
    return render(request, 'frontend/menu.html', context)
# frontend/views.py の続きに追加

@login_required
def calendar_view(request):
    return render(request, 'frontend/calendar.html')