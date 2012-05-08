from django.contrib import admin
from django.db import models
from manifest.models import ConfigCar, Manifest, ManifestCargo, ManifestCargoPay, ManifestRecevier
    
class ManifestAdmin(admin.ModelAdmin):
    list_display = ('toro_m_number', 'toro_m_origin_city', 'toro_m_destiny_city')
    
class ManifestCargoAdmin(admin.ModelAdmin):
    list_display = ('toro_mf_id', 'toro_mf_pay_date')
    
class ManifestCargoPayAdmin(admin.ModelAdmin):
    list_display = ('toro_cd_id_city', 'toro_cd_name_city', 'toro_cd_dpto')
    
class ManifestRecevierAdmin(admin.ModelAdmin):
    list_display = ('toro_cd_id_city', 'toro_cd_name_city', 'toro_cd_dpto')

    
admin.site.register(ConfigCar)
admin.site.register(ManifestCargo, ManifestCargoAdmin)
admin.site.register(ManifestCargoPay, ManifestCargoPayAdmin)
admin.site.register(ManifestRecevier, ManifestRecevierAdmin)