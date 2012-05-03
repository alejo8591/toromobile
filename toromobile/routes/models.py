# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, time
from city.models import CodeDane, CodeDANE
        
class RouteDestiny(CodeDane):
    #Uppercase
    def save(self, *args, **kwargs):
            self.toro_cd_name_city = self.toro_cd_name_city.upper()
            self.toro_cd_dpto = self.toro_cd_dpto.upper()
            super(RouteDestiny, self).save(*args, **kwargs)
            
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_cd_id_city, self.toro_cd_name_city, self.toro_cd_dpto)
    class Meta:
        ordering = ['toro_cd_name_city']
        verbose_name = "Ciudades de destino"

    
class Route(models.Model):
    toro_r_name = models.CharField(max_length= 10, verbose_name='Número Ruta',  help_text='Número de la Ruta según cronograma de envión', unique=True)
    toro_r_origin = models.ForeignKey(CodeDANE, verbose_name='Ciudad Origen',  help_text='Código de la ciudad Origen según el DANE')
    toro_r_destiny = models.ForeignKey(RouteDestiny, verbose_name='Ciudad Destino',  help_text='Código de la ciudad Destino según el DANE')
    
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_r_name, self.toro_r_origin, self.toro_r_destiny)
    class Meta:
        ordering = ['toro_r_name']
        verbose_name = "Ruta"