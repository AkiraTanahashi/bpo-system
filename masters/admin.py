from django.contrib import admin
from .models import MedicalInstitution, CareManager, AccountingFirm

@admin.register(MedicalInstitution)
class MedicalInstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'specialty_code', 'company_label')
    list_filter = ('company',)
    search_fields = ('name', 'code')

    # 共通マスタか個別か分かりやすく表示
    def company_label(self, obj):
        return obj.company.name if obj.company else "【共通マスタ】"
    company_label.short_description = "所属法人"

@admin.register(CareManager)
class CareManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'office_name', 'contact_info', 'company')
    list_filter = ('company',)
    search_fields = ('name', 'office_name')

@admin.register(AccountingFirm)
class AccountingFirmAdmin(admin.ModelAdmin):
    list_display = ('name', 'firm_code', 'contract_status', 'company')
    list_filter = ('contract_status', 'company')