from django.contrib import admin
from django.db import models
from routes.models import Route, RouteDestiny

class RouteAdmin(admin.ModelAdmin):
    list_display = ('toro_r_name', 'toro_r_origin', 'toro_r_destiny')
    
class RouteDestinyAdmin(admin.ModelAdmin):
    list_display = ('toro_cd_id_city', 'toro_cd_name_city', 'toro_cd_dpto')
 
#Adicionando a django admin 
admin.site.register(Route, RouteAdmin)
admin.site.register(RouteDestiny, RouteDestinyAdmin)