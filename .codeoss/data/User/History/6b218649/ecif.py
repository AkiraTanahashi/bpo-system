from django.db import models
import uuid
from django.conf import settings  # ユーザー情報と紐付けるため
from django.utils.translation import gettext_lazy as _
from clients.models import Company

# 1. 操作ログ (Operation_Log)
class OperationLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # 誰が (User)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name=_("実行ユーザー"))
    # どの会社のデータで (Company)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("対象法人"))
    
    # 何をしたか
    ACTION_CHOICES = (
        ('LOGIN', _('ログイン')),
        ('LOGOUT', _('ログアウト')),
        ('CREATE', _('作成')),
        ('UPDATE', _('更新')),
        ('DELETE', _('削除')),
        ('EXPORT', _('データ出力')),
        ('OTHER', _('その他')),
    )
    action_type = models.CharField(_("操作タイプ"), max_length=20, choices=ACTION_CHOICES)
    detail = models.TextField(_("詳細内容"), blank=True) # 具体的に何をいじったか
    
    # いつ、どこで
    ip_address = models.GenericIPAddressField(_("IPアドレス"), null=True, blank=True)
    created_at = models.DateTimeField(_("実行日時"), auto_now_add=True) # timestamp

    def __str__(self):
        return f"{self.get_action_type_display()} - {self.user} ({self.created_at})"

    class Meta:
        verbose_name = _("操作ログ")
        verbose_name_plural = _("操作ログ一覧")
        ordering = ['-created_at'] # 新しい順に表示

# 2. 勤怠ログ (Attendance_Log)
class AttendanceLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("職員"))
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("所属法人"))
    
    # 出退勤時間
    clock_in_time = models.DateTimeField(_("出勤時間"), null=True, blank=True)
    clock_out_time = models.DateTimeField(_("退勤時間"), null=True, blank=True)
    
    # 位置情報 (GPS等) - テキストで保存 (例: "35.6895, 139.6917")
    location_data = models.CharField(_("位置情報"), max_length=100, blank=True)
    
    # 備考 (遅延理由など)
    note = models.TextField(_("備考"), blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.clock_in_time}"

    class Meta:
        verbose_name = _("勤怠記録")
        verbose_name_plural = _("勤怠ログ一覧")