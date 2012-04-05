# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms.extras.widgets import SelectDateWidget
from car.models import Car, CarBodyWork, CarColor, CarLine, CarMandated, CarMark, CarOwner
from car.SelectTimeWidget import SelectTimeWidget

class CarAdmin(admin.ModelAdmin):
    #Cambiando modo en el que se ve el TimeField con respecto al admin de django
    timefield = SelectTimeWidget(twelve_hr=True)
    formfield_overrides={
        models.TimeField: {'widget': timefield},
        #Cambiando la manera de ver el DateTime con respecto al admin    
        models.DateField: {'widget': SelectDateWidget}
    }
    list_display = ('toro_car_plate', 'toro_car_bodyWork')
    
class CarAdmin(admin.ModelAdmin):
    #Cambiando modo en el que se ve el TimeField con respecto al admin de django
    timefield = SelectTimeWidget(twelve_hr=True)
    formfield_overrides={
        models.TimeField: {'widget': timefield},
        #Cambiando la manera de ver el DateTime con respecto al admin    
        models.DateField: {'widget': SelectDateWidget}
    }
    list_display = ('toro_car_plate', 'toro_car_bodyWork')

class CarAdmin(admin.ModelAdmin):
    #Cambiando modo en el que se ve el TimeField con respecto al admin de django
    timefield = SelectTimeWidget(twelve_hr=True)
    formfield_overrides={
        models.TimeField: {'widget': timefield},
        #Cambiando la manera de ver el DateTime con respecto al admin    
        models.DateField: {'widget': SelectDateWidget}
    }
    list_display = ('toro_car_plate', 'toro_car_bodyWork')
    
class CarAdmin(admin.ModelAdmin):
    #Cambiando modo en el que se ve el TimeField con respecto al admin de django
    timefield = SelectTimeWidget(twelve_hr=True)
    formfield_overrides={
        models.TimeField: {'widget': timefield},
        #Cambiando la manera de ver el DateTime con respecto al admin    
        models.DateField: {'widget': SelectDateWidget}
    }
    list_display = ('toro_car_plate', 'toro_car_bodyWork')
    
class CarAdmin(admin.ModelAdmin):
    #Cambiando modo en el que se ve el TimeField con respecto al admin de django
    timefield = SelectTimeWidget(twelve_hr=True)
    formfield_overrides={
        models.TimeField: {'widget': timefield},
        #Cambiando la manera de ver el DateTime con respecto al admin    
        models.DateField: {'widget': SelectDateWidget}
    }
    list_display = ('toro_car_plate', 'toro_car_bodyWork')
    
class CarAdmin(admin.ModelAdmin):
    #Cambiando modo en el que se ve el TimeField con respecto al admin de django
    timefield = SelectTimeWidget(twelve_hr=True)
    formfield_overrides={
        models.TimeField: {'widget': timefield},
        #Cambiando la manera de ver el DateTime con respecto al admin    
        models.DateField: {'widget': SelectDateWidget}
    }
    list_display = ('toro_car_plate', 'toro_car_bodyWork')
    
class CarAdmin(admin.ModelAdmin):
    #Cambiando modo en el que se ve el TimeField con respecto al admin de django
    timefield = SelectTimeWidget(twelve_hr=True)
    formfield_overrides={
        models.TimeField: {'widget': timefield},
        #Cambiando la manera de ver el DateTime con respecto al admin    
        models.DateField: {'widget': SelectDateWidget}
    }
    list_display = ('toro_car_plate', 'toro_car_bodyWork')

admin.site.register(Car, CarAdmin)