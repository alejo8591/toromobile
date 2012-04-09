# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from city.models import CodeDane, CodeDANE
from car.models import CarPlate, CarTrailer, Car
from driver.models import CarDriver
from company.models import Company
"""
    Este modelo se hace con base a la documento del Ministerio de Trasporte
    Direccion de transito y transporte, Sistema de Información para la generación del
    Manifiesto de Cargas "SIMCA".
    El siguiente modelo hace referencia a "Archivo plano maestro de manifiesto"
"""
#Configuración el Vehiculo
class ConfigCar(models.Model):
    toro_cc_id = models.CharField(max_length=13, unique=True, verbose_name='Designación', help_text="Desginación de la configuración según norma")
    toro_cc_scheme = models.ImageField(verbose_name='Esquema', help_text="Imagen Referente al Esquema del Tipo de Carro")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cc_id, self.toro_cc_scheme)
    class Meta:
        ordering = ['toro_cd_name_city']
        verbose_name = "Códigos DANE ciudades de envio"
#Heredando de CodeDane para ingresar los codigos
class ManifestRecevier(CodeDane):
    #Código asignado de la ciudad, municipio, casrio según DANE
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_cd_id_city, self.toro_cd_name_city, self.toro_cd_dpto)
    class Meta:
        ordering = ['toro_cd_name_city']
        verbose_name = "Códigos DANE ciudades de envio"
        
class ManifestCargoPay(CodeDane):
    #Código asignado de la ciudad, municipio, casrio según DANE
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_cd_id_city, self.toro_cd_name_city, self.toro_cd_dpto)
    class Meta:
        ordering = ['toro_cd_name_city']
        verbose_name = "Códigos DANE ciudades pago"

class ManifestCargo(models.Model):
    #El flete se debe amarrar a una empresa
    toro_mf_id = models.ManyToManyField(Company, verbose_name='Empresa(s)', help_text="Empresa(s) se les realiza el Envio")
    toro_mf_retefuente = models.FloatField(max_length=20, verbose_name='Rete-Fuente', help_text="Retención en la Fuente")
    toro_mf_reteica = models.FloatField(max_length=20, verbose_name='ICA', help_text="Retención ICA")
    toro_mf_net_pay = models.FloatField(max_length=20, verbose_name='Pago Neto', help_text="Valor Neto a Pagar")
    toro_mf_advanced = models.FloatField(max_length=20, verbose_name='Valor Anticipo', help_text="valor que la empresa paga por adelantado")
    toro_mf_balance_due = models.FloatField(max_length=20,verbose_name='Por Pagar', help_text="Diferencia entre valor neto y el valor del anticipo")
    toro_mf_total_letter = models.CharField(max_length=120, verbose_name='Total en letras', help_text="Se registra en letras el valor total del viaje")
    toro_mf_pay_city = models.ForeingKey(ManifestCargoPay, verbose_name='Ciudad Pago', help_text="Lugar en el cual será pagado el saldo del valor del viaje.")
    toro_mf_pay_date = models.DatetimeField(verbose_name='Fecha Pago', help_text="a fecha para el pago del saldo del valor del viaje")
    
    def __unicode__(self):
       return u'%s %s' %(self.toro_mf_id, self.toro_mf_pay_date)
    class Meta:
        ordering = ['toro_mf_id']
        verbose_name = "Datos de flete"

class Manifest(models.Model):
    toro_m_number = models.CharField(max_length=13, verbose_name='Número Manifiesto', help_text="Número expedido del Manifiesto")
    toro_m_date = models.DateTimeField(verbose_name='Fecha Manifiesto', help_text="Fecha de expedición del Manifiesto")
    toro_m_origin_city = models.ForeignKey(CodeDANE,verbose_name='Ciudad Origen', help_text="Ciudad de Origen según codigo del DANE")
    toro_m_destiny_city = models.ForeignKey(ManifestRecevier, verbose_name='Ciudad Destino', help_text="Ciudad de Destino según codigo del DANE")
    toro_m_car_plate = models.ForeignKey(Car, verbose_name='Placa Vehículo', help_text="Placa del vehiculo Transportador")
    toro_m_driver_type_id = models.ForeignKey(CarDriver, verbose_name='Datos Conductor', help_text="Datos correspondientes al conductor")
    toro_m_trailer = models.ForeignKey(CarTrailer, verbose_name='Placa Vehículo', help_text="Placa del vehiculo Transportador")
    toro_m_config = models.ForeignKey(ConfigCar, verbose_name='Cofiguración', help_text="Configuración del Vehiculo")
    toro_m_cargo = models.ForeignKey(ManifestCargo, verbose_name='Cofiguración', help_text="Configuración del Vehiculo")
    toro_m_name_cargo = models.CharField(max_length=120, verbose_name='Cargue y Descargue', help_text="Nombre de quien cancela este valor, de conformidad con la Resolución No. 870")
    toro_m_date_created = models.DateField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación del manifiesto')
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_m_number, self.toro_m_origin_city, self.toro_m_destiny_city)
    class Meta:
        ordering = ['toro_m_date']
        verbose_name = "Manifiesto de Carga"    