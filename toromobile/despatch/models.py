# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, time
from car.models import *
from city.models import CodeDANE, CodeDane
from company.models import *
from driver.models import CarDriver
from routes.models import Route
from packet.models import Package

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
    #normal, medio, alto nivel
    toro_dcic_security = models.IntegerField(max_length=1, choices=((1,'Normal'),(2, 'Medio'), (3, 'Alto') ), verbose_name='Nivel Seguimiento', help_text="Nivel de seguimiento según tipo de Carga")
    toro_dcic_date_despatch = models.DateTimeField(verbose_name='Nivel Seguimiento', help_text="Nivel de seguimiento según tipo de Carga")

    def __unicode__(self):
       return u'%s %s' %(self.toro_dcic_route, self.toro_dcic_date_despatch)
    class Meta:
        ordering = ['toro_dcic_date_despatch']
        verbose_name = "Información de CIC y Ruta"
#Precintos
class DespatchSeal(models.Model):
    toro_ds_seal = models.IntegerField(max_length=10, unique=True, verbose_name='Número Precinto', help_text="Número del o los Precintos para cada Camion")
    toro_ds_observation = models.TextField(verbose_name='Observación Precinto', help_text="Indicar la Placa del Carro o alguna observación")
    toro_ds_date_created = models.DateField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación del manifiesto')

    def __unicode__(self):
       return u'%s %s' %(self.toro_ds_seal, self.toro_ds_date_created)
    class Meta:
        ordering = ['toro_ds_date_created']
        verbose_name = "Carga de Precinto"

class DespatchCharge(models.Model):
    toro_dc_manifest =  models.ForeignKey(Package, verbose_name='Número Manifiesto', help_text="Paquetes y Número del Manifiesto")
    toro_dc_route = models.ForeignKey(Route, verbose_name='Ruta', help_text="Ruta del despacho")
    toro_dc_car_plate = models.ForeignKey(Car, verbose_name='Placa Vehículo', help_text="Placa del vehiculo Transportador")
    toro_dc_driver_id = models.ManyToManyField(CarDriver, verbose_name='Datos Conductor', help_text="Datos correspondientes al conductor")
    toro_dc_name_cargo = models.CharField(max_length=120, verbose_name='Cargue y Descargue', help_text="Nombre de quien cancela este valor, de conformidad con la Resolución No. 870")
    toro_dc_cargo = models.ForeignKey(DespatchCargo, verbose_name='Datos adicionales', help_text="Datos de pago y generación de costos")
    toro_dc_cic = models.ForeignKey(DespatchCIC, verbose_name='Datos CIC', help_text="Información CIC (Centro de Información y Control)")
    toro_dc_seal = models.ManyToManyField(DespatchSeal, verbose_name='Datos Precinto', help_text="Elija los Precintos para el Carro o Remolque")
    toro_dc_observation = models.TextField(verbose_name='Observación', help_text="Observación del Despacho")
    toro_dc_date_created = models.DateField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación del manifiesto')

    
    def __unicode__(self):
       return u'%s %s' %(self.toro_dc_manifest, self.toro_dc_date_created)
    class Meta:
        ordering = ['toro_dc_date_created']
        verbose_name = "Despacho"