from django.contrib import admin
from django.db import models
from driver.models import CarDriver

class CarDriverAdmin(admin.ModelAdmin):
    list_display = ('toro_cd_id', 'toro_cd_first_name', 'toro_cd_name')
    
admin.site.register(CarDriver, CarDriverAdmin)