# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.
class CodeDane(models.Model):
    #Código asignado de la ciudad, municipio, casrio según DANE
    toro_cd_id_city = models.IntegerField(max_length=10, verbose_name='Código Ciudad', help_text="Código de identificación de la ciudad según DANE", unique=True)
    toro_cd_name_city = models.CharField(max_length=20, verbose_name='Nombre Ciudad', help_text="Nombre de la ciudad, municipio, cacerio según DANE")
    toro_cd_dpto = models.CharField(max_length=20, verbose_name='Nombre Departamento', help_text="Nombre de identificación de la ciudad según DANE")
            
    class Meta:
        abstract = True
                    
class CodeDANE(CodeDane):
    #Uppercase
    def save(self, *args, **kwargs):
            self.toro_cd_name_city = self.toro_cd_name_city.upper()
            self.toro_cd_dpto = self.toro_cd_dpto.upper()
            super(CodeDANE, self).save(*args, **kwargs)
            
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_cd_id_city, self.toro_cd_name_city, self.toro_cd_dpto)
       
    class Meta:
        ordering = ['toro_cd_name_city']
        verbose_name = "Códigos DANE ciudade"
        
