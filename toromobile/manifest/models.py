# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from city.models import CodeDane, CodeDANE
from car.models import CarPlate
from driver.models import CarDriver
"""
    Este modelo se hace con base a la documento del Ministerio de Trasporte
    Direccion de transito y transporte, Sistema de Información para la generación del
    Manifiesto de Cargas "SIMCA".
    El siguiente modelo hace referencia a "Archivo plano maestro de manifiesto"
"""
class ManifestRecevier(CodeDane):
    #Código asignado de la ciudad, municipio, casrio según DANE
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_cd_id_city, self.toro_cd_name_city, self.toro_cd_dpto)
    class Meta:
        ordering = ['toro_cd_name_city']
        verbose_name = "Códigos DANE ciudade"

class Manifest(models.Model):
    toro_m_number = models.CharField(max_length=13, verbose_name='Número Manifiesto', help_text="Número expedido del Manifiesto")
    toro_m_date = models.DateTimeField(verbose_name='Fecha Manifiesto', help_text="Fecha de expedición del Manifiesto")
    toro_m_origin_city = models.ForeignKey(CodeDANE,verbose_name='Ciudad Origen', help_text="Ciudad de Origen según codigo del DANE")
    toro_m_destiny_city = models.ForeignKey(ManifestRecevier, verbose_name='Ciudad Destino', help_text="Ciudad de Destino según codigo del DANE")
    toro_m_car_plate = models.ForeignKey(CarPlate, verbose_name='Placa Vehículo', help_text="Placa del vehiculo Transportador")
    toro_m_driver_type_id = models.ForeignKey(CarDriver)