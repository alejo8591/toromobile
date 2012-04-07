from django.contrib import admin
from django.db import models
from driver.models import CodeDane
from company.models import Company, CompanyShipping

class CompanyShippingAdmin(admin.ModelAdmin):
    list_display = ('toro_cs_date_creation', 'toro_cs')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('toro_c_id', 'toro_c_name', 'toro_c_city', 'toro_c_phone')
    
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyShipping, CompanyShippingAdmin)