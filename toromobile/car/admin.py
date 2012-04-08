# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms.extras.widgets import SelectDateWidget
from car.models import Car, CarBodyWork, CarColor, CarLine, CarMandated, CarMark, CarOwner, CarTrailer, CarPlate
from car.SelectTimeWidget import SelectTimeWidget
    
class CarBodyWorkAdmin(admin.ModelAdmin):
    list_display = ('toro_cbw_code', 'toro_cbw_description')

class CarColorAdmin(admin.ModelAdmin):
    list_display = ('toro_cc_code', 'toro_cc_description')
    
class CarLineAdmin(admin.ModelAdmin):
    list_display = ('toro_cl_code', 'toro_cl_description')
    
class CarMandatedAdmin(admin.ModelAdmin):
    list_display = ('toro_cm_type_id', 'toro_cm_first_name', 'toro_cm_last_name')
    
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('toro_cm_code', 'toro_cm_code')

class CarOwnerAdmin(admin.ModelAdmin):
    list_display = ('toro_co_type_id', 'toro_co_first_name', 'toro_co_last_name')
    
class CarTrailerAdmin(admin.ModelAdmin):
    list_display = ('toro_ct_id', 'toro_ct_description')

class CarAdmin(admin.ModelAdmin):
    #Cambiando modo en el que se ve el TimeField con respecto al admin de django
    timefield = SelectTimeWidget(twelve_hr=True)
    formfield_overrides={
        models.TimeField: {'widget': timefield},
        #Cambiando la manera de ver el DateTime con respecto al admin    
        models.DateField: {'widget': SelectDateWidget}
    }
    list_display = ('toro_car_plate', 'toro_car_date_created')
    
class CarPlateAdmin(admin.ModelAdmin):
    list_display = ('toro_cp_plate', 'toro_cp_plate_city')
 
#Adicionando a django admin 
admin.site.register(CarBodyWork, CarBodyWorkAdmin)
admin.site.register(CarColor, CarColorAdmin)
admin.site.register(CarLine, CarLineAdmin)
admin.site.register(CarMandated, CarMandatedAdmin)
admin.site.register(CarMark, CarMarkAdmin)
admin.site.register(CarOwner, CarOwnerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarTrailer, CarTrailerAdmin)
admin.site.register(CarPlate, CarPlateAdmin)