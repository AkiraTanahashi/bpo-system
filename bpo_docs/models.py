from django.db import models
import uuid
# clientsアプリから会社・施設情報を借りる
from clients.models import Company, Facility 

class Document(models.Model):
    # 文書の種類
    DOC_TYPES = (
        ('RECEIPT', 'レシート・領収書'),
        ('INVOICE', '請求書'),
        ('CONTRACT', '契約書'),
        ('REPORT', '日報・介護記録'),
        ('SALARY', '給与明細'),
        ('OTHER', 'その他'),
    )

    # ステータス
    STATUS_CHOICES = (
        ('PENDING', '解析待ち'),
        ('PROCESSING', 'AI解析中'),
        ('CONFIRMED', '確認済み'),
        ('APPROVED', '承認完了'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # マルチテナント紐付け
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="法人")
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="施設")

    # ファイル本体
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name="ファイル")
    
    doc_type = models.CharField("文書タイプ", max_length=20, choices=DOC_TYPES)
    status = models.CharField("ステータス", max_length=20, choices=STATUS_CHOICES, default='PENDING')

    # AI解析データ保存用（JSON）
    ai_data = models.JSONField("AI解析データ", default=dict, blank=True)
    
    created_at = models.DateTimeField("アップロード日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return f"{self.get_doc_type_display()} - {self.company.name}"

    class Meta:
        verbose_name = "ドキュメント"
        verbose_name_plural = "ドキュメント一覧"