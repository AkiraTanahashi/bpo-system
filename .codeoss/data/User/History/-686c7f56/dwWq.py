from django.db import models
import uuid
# 翻訳用の関数をインポート（これが「_」の正体です）
from django.utils.translation import gettext_lazy as _

# 1. 会社（法人）モデル
class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # 文字列を _("...") で囲むことで、後で辞書登録できるようになります
    name = models.CharField(_("法人名"), max_length=100)
    code = models.CharField(_("法人コード"), max_length=20, unique=True)
    address = models.CharField(_("住所"), max_length=200, blank=True)
    created_at = models.DateTimeField(_("登録日"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("法人")
        verbose_name_plural = _("法人一覧")

# 2. 施設（事業所）モデル
class Facility(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("所属法人"))
    name = models.CharField(_("施設名"), max_length=100)
    code = models.CharField(_("施設コード"), max_length=20, unique=True)
    is_active = models.BooleanField(_("契約中"), default=True)
    
    def __str__(self):
        return f"{self.company.name} - {self.name}"

    class Meta:
        verbose_name = _("施設")
        verbose_name_plural = _("施設一覧")
# clients/models.py の続き（既存のCompany, Facilityの下に追加）

# Djangoの標準ユーザーと紐付けるためにインポート
from django.conf import settings 

# 3. 介護利用者・対象者 (Patient/Client)
class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("所属法人"))
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("利用施設"))
    
    # ER図: insured_number_encrypted, name, address
    name = models.CharField(_("利用者名"), max_length=100)
    name_kana = models.CharField(_("カナ氏名"), max_length=100, blank=True)
    
    # 実際は暗号化して保存推奨ですが、まずは箱を用意
    insured_number = models.CharField(_("被保険者番号"), max_length=20, blank=True)
    
    birth_date = models.DateField(_("生年月日"), null=True, blank=True)
    address = models.CharField(_("住所"), max_length=200, blank=True)
    
    created_at = models.DateTimeField(_("登録日"), auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.insured_number})"

    class Meta:
        verbose_name = _("介護利用者")
        verbose_name_plural = _("利用者マスタ")

# 4. 職員プロフィール (Staff/User Profile)
# Django標準の「User」と「Company」を繋ぐ接着剤の役割
class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='staff_profile', verbose_name=_("ログインユーザー"))
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("所属法人"))
    
    # ER図: role_id, plan_status
    role_choices = (
        ('ADMIN', _('管理者')),
        ('MANAGER', _('施設長')),
        ('STAFF', _('一般職員')),
        ('PART', _('パート・アルバイト')),
    )
    role = models.CharField(_("権限ロール"), max_length=20, choices=role_choices, default='STAFF')
    
    joined_at = models.DateField(_("入社日"), null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.company.name}"

    class Meta:
        verbose_name = _("職員情報")
        verbose_name_plural = _("職員管理")