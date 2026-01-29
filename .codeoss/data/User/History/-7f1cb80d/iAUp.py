from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from clients.models import Company, Facility 

class Document(models.Model):
    # 選択肢の文言も翻訳対象にします
    DOC_TYPES = (
        ('RECEIPT', _('レシート・領収書')),
        ('INVOICE', _('請求書')),
        ('CONTRACT', _('契約書')),
        ('REPORT', _('日報・介護記録')),
        ('SALARY', _('給与明細')),
        ('OTHER', _('その他')),
    )

    STATUS_CHOICES = (
        ('PENDING', _('解析待ち')),
        ('PROCESSING', _('AI解析中')),
        ('CONFIRMED', _('確認済み')),
        ('APPROVED', _('承認完了')),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("法人"))
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("施設"))

    file = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name=_("ファイル"))
    
    doc_type = models.CharField(_("文書タイプ"), max_length=20, choices=DOC_TYPES)
    status = models.CharField(_("ステータス"), max_length=20, choices=STATUS_CHOICES, default='PENDING')

    ai_data = models.JSONField(_("AI解析データ"), default=dict, blank=True)
    
    created_at = models.DateTimeField(_("アップロード日時"), auto_now_add=True)
    updated_at = models.DateTimeField(_("更新日時"), auto_now=True)

    def __str__(self):
        # ここはデータの中身なので翻訳しなくてOK
        return f"{self.get_doc_type_display()} - {self.company.name}"

    class Meta:
        verbose_name = _("ドキュメント")
        verbose_name_plural = _("ドキュメント一覧")