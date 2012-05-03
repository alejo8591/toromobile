# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, time
from car.models import *
from city.models import CodeDANE, CodeDane
from company.models import *
from driver.models import CarDriver
from routes.models import Route


"""
    Este modelo se hace con base a la documento del Ministerio de Trasporte
    Direccion de transito y transporte, Sistema de Información para la generación del
    Manifiesto de Cargas "SIMCA".
    El siguiente modelo hace referencia a "Archivo plano maestro de manifiesto"
"""
        
class DespatchCargo(models.Model):
    #El flete se debe amarrar a una empresa
    toro_dca_id = models.ForeignKey(Company, verbose_name='Empresa(s)', help_text="Empresa(s) se les realiza el Envio")
    toro_dca_retefuente = models.FloatField(max_length=20, verbose_name='Rete-Fuente', help_text="Retención en la Fuente")
    toro_dca_reteica = models.FloatField(max_length=20, verbose_name='ICA', help_text="Retención ICA")
    toro_dca_net_pay = models.FloatField(max_length=20, verbose_name='Pago Neto', help_text="Valor Neto a Pagar")
    toro_dca_advanced = models.FloatField(max_length=20, verbose_name='Valor Anticipo', help_text="valor que la empresa paga por adelantado")
    toro_dca_balance_due = models.FloatField(max_length=20,verbose_name='Por Pagar', help_text="Diferencia entre valor neto y el valor del anticipo")
    toro_dca_total_letter = models.CharField(max_length=120, verbose_name='Total en letras', help_text="Se registra en letras el valor total del viaje")
    #toro_dca_pay_city = models.ForeignKey(ManifestCargoPay, verbose_name='Ciudad Pago', help_text="Lugar en el cual será pagado el saldo del valor del viaje.")
    toro_dca_pay_date = models.DateTimeField(verbose_name='Fecha Pago', help_text="a fecha para el pago del saldo del valor del viaje")
    
    def __unicode__(self):
       return u'%s %s' %(self.toro_dca_id, self.toro_dca_pay_date)
    class Meta:
        ordering = ['toro_dca_pay_date']
        verbose_name = "Datos de flete"
        
class DespatchCIC(models.Model):
    toro_dcic_route = models.ForeignKey(Route, verbose_name='Ruta', help_text="Número de Ruta esptipulada para el despacho")
    toro_dcic = models.CharField(max_length=120, verbose_name='Total en letras', help_text="Se registra en letras el valor total del viaje")


class DespatchCharge(models.Model):
    toro_dc_route = models.ForeignKey(Route, verbose_name='Ruta', help_text="Ruta del despacho")
    toro_dc_car_plate = models.ForeignKey(Car, verbose_name='Placa Vehículo', help_text="Placa del vehiculo Transportador")
    toro_dc_driver_id = models.ForeignKey(CarDriver, verbose_name='Datos Conductor', help_text="Datos correspondientes al conductor")
    toro_dc_name_cargo = models.CharField(max_length=120, verbose_name='Cargue y Descargue', help_text="Nombre de quien cancela este valor, de conformidad con la Resolución No. 870")
    toro_dc_date_created = models.DateField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación del manifiesto')