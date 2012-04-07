from django.contrib import admin
from django.db import models
from driver.models import CodeDane
from package.models import Package, PackageProduct

class PackageAdmin(admin.ModelAdmin):
    list_display = ('toro_p_manifest', 'toro_p_name_shipping', 'toro_p_name_receiver', 'toro_p_city_receiver')

class PackageProductAdmin(admin.ModelAdmin):
    list_display = ('toro_pp_id', 'toro_pp_description')
    
admin.site.register(Package, PackageAdmin)
admin.site.register(PackageProduct, PackageProductAdmin)

