# clients/admin.py
from django.contrib import admin
from .models import Company, Facility,Client, Staff

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


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'insured_number', 'company', 'facility')
    list_filter = ('company', 'facility')
    search_fields = ('name', 'insured_number')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'role', 'joined_at')
    list_filter = ('company', 'role')
    search_fields = ('user__username', 'company__name')