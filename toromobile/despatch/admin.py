from django.contrib import admin
from django.db import models
from despatch.models import DespatchCargo, DespatchCharge, DespatchCIC, DespatchSeal

class DespatchCargoAdmin(admin.ModelAdmin):
    list_display = ('toro_dca_id', 'toro_dca_pay_date')
    
class DespatchChargeAdmin(admin.ModelAdmin):
    list_display = ('toro_dc_manifest', 'toro_dc_date_created')
    filter_horizontal = ('toro_dc_driver_id',)

class DespatchCICAdmin(admin.ModelAdmin):
    list_display = ('toro_dcic_route', 'toro_dcic_date_despatch')

class DespatchSealAdmin(admin.ModelAdmin):
    list_display = ('toro_ds_seal', 'toro_ds_date_created')

admin.site.register(DespatchCargo, DespatchCargoAdmin)
admin.site.register(DespatchCharge, DespatchChargeAdmin)
admin.site.register(DespatchCIC, DespatchCICAdmin)
admin.site.register(DespatchSeal, DespatchSealAdmin)