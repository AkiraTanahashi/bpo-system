from django.contrib import admin
from .models import OperationLog, AttendanceLog

@admin.register(OperationLog)
class OperationLogAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'action_type', 'user', 'company', 'ip_address')
    list_filter = ('action_type', 'company', 'created_at')
    search_fields = ('user__username', 'detail', 'ip_address')
    
    # ログは基本的に変更させない (ReadOnly)
    readonly_fields = ('created_at', 'user', 'company', 'action_type', 'detail', 'ip_address')

    def has_add_permission(self, request):
        # 管理画面から手動でログを追加することは禁止（システムが自動追加するため）
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(AttendanceLog)
class AttendanceLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'clock_in_time', 'clock_out_time', 'location_data')
    list_filter = ('company', 'clock_in_time')
    search_fields = ('user__username',)
    
     # ログは基本的に変更させない (ReadOnly)
    readonly_fields = ('created_at', 'user', 'company', 'action_type', 'detail', 'ip_address')

    def has_add_permission(self, request):
        # 管理画面から手動でログを追加することは禁止（システムが自動追加するため）
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False