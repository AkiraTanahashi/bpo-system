# clients/admin.py
from django.contrib import admin
from .models import Company, Facility

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'address', 'created_at')
    search_fields = ('name', 'code')
    ordering = ('code',)

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'company', 'is_active')
    list_filter = ('company', 'is_active')
    search_fields = ('name', 'code')
    autocomplete_fields = ['company']