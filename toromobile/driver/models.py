# -*- coding: utf-8 -*-
from django.db import models
from city.models import CodeDANE
from datetime import datetime, time
"""
    Este modelo se hace con base a la documento del Ministerio de Trasporte
    Direccion de transito y transporte, Sistema de Información para la generación del
    Manifiesto de Cargas "SIMCA".
    El siguiente modelo hace referencia a "Archivo plano maestro de personas"
"""
#Modelo referente a los datos del conductor    
class CarDriver(models.Model):
    toro_cd_type_id = models.IntegerField(max_length= 2, choices=((1, 'Cédula'),(2, 'NIT'),(3, 'Extranjería')), verbose_name='Tipo de identificación', help_text="Tipo de identificación del conductor")
    toro_cd_id = models.CharField(max_length=20, verbose_name='Número identificación', help_text="Número de identificación del conductor del vehiculo")
    toro_cd_first_name = models.CharField(max_length=12, verbose_name='Primer Apellido', help_text="Primer Apellido del conductor")
    toro_cd_second_name = models.CharField(max_length=12, verbose_name='Segundo Apellido', help_text="Sengundo Apellido del conductor")
    toro_cd_name = models.CharField(max_length=20, verbose_name='Nombre(s)', help_text="Nombre(s) del conductor del vehiculo")
    toro_cd_phone = models.IntegerField(max_length=10, verbose_name='Telefono', help_text="Número telefonico del conductor del vehiculo")
    toro_cd_address = models.CharField(max_length=40, verbose_name='Dirección', help_text="Dirección de contacto del conductor del vehiculo")
    toro_cd_license = models.IntegerField(max_length= 2, choices=((4, '4'),(5, '5'),(6, '6')), verbose_name='Categoria Licencia', help_text="Categoria de la licencia 4, 5 ó 6")
    toro_cd_codedane = models.ForeignKey(CodeDANE, verbose_name='Ciudad',  help_text='Código de la ciudad según el DANE')
    #Optimización para ver en el admin site de Django
    def __unicode__(self):
       return u'%s %s %s %s' %(self.toro_cd_id, self.toro_cd_first_name, self.toro_cd_name)
    class Meta:
        ordering = ['toro_cd_id']
        verbose_name = "Datos conductore"
