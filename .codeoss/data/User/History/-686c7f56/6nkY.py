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