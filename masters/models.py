from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
# DBA（Clientsアプリ）から会社情報を参照
from clients.models import Company 

# 1. 医療機関マスタ (Medical_Institution)
class MedicalInstitution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # companyが空(null)なら「共通マスタ」、入っていれば「その会社専用マスタ」
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("法人"))
    
    # ER図: inst_id, inst_name, postal_code, specialty_code
    code = models.CharField(_("医療機関コード"), max_length=20) # inst_id
    name = models.CharField(_("医療機関名"), max_length=100)    # inst_name
    postal_code = models.CharField(_("郵便番号"), max_length=8, blank=True)
    specialty_code = models.CharField(_("診療科コード"), max_length=20, blank=True)
    
    created_at = models.DateTimeField(_("登録日"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("医療機関")
        verbose_name_plural = _("医療機関マスタ")

# 2. ケアマネジャー・事業所マスタ (Care_Manager)
class CareManager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("法人"))
    
    # ER図: manager_id, contact_info, office_id
    name = models.CharField(_("氏名"), max_length=100) # manager_id (表示用)
    code = models.CharField(_("担当者コード"), max_length=20, blank=True)
    contact_info = models.CharField(_("連絡先"), max_length=100, blank=True) # 電話番号など
    office_name = models.CharField(_("所属事業所名"), max_length=100) # office_id (表示用)

    created_at = models.DateTimeField(_("登録日"), auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.office_name})"

    class Meta:
        verbose_name = _("ケアマネジャー")
        verbose_name_plural = _("ケアマネマスタ")

# 3. 会計事務所マスタ (Accounting_Firm)
class AccountingFirm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("法人"))
    
    # ER図: firm_id, contract_status
    name = models.CharField(_("事務所名"), max_length=100)
    firm_code = models.CharField(_("事務所コード"), max_length=20) # firm_id
    
    # 契約状態（選択式）
    STATUS_CHOICES = (
        ('ACTIVE', _('契約中')),
        ('PENDING', _('調整中')),
        ('EXPIRED', _('解約済')),
    )
    contract_status = models.CharField(_("契約ステータス"), max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    
    created_at = models.DateTimeField(_("登録日"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("会計事務所")
        verbose_name_plural = _("会計事務所マスタ")