from django.contrib import admin
from django.db import models
from city.models import CodeDANE

class CodeDANEAdmin(admin.ModelAdmin):
    list_display = ('toro_cd_id_city', 'toro_cd_name_city', 'toro_cd_dpto')
    
admin.site.register(CodeDANE, CodeDANEAdmin)