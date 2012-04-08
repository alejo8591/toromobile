# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
#from django.db.models.fields.related import ForeignKey, ManyToOneRel 
from city.models import CodeDANE

"""
    Este modelo se hace con base a la documento del Ministerio de Trasporte
    Direccion de transito y transporte, Sistema de Información para la generación del
    Manifiesto de Cargas "SIMCA".
    El siguiente modelo hace referencia a "Archivo plano maestro de empresas"
"""
#Direcciones de envio para las empresas
class CompanyShipping(models.Model):
    toro_cs = models.CharField(max_length=40, verbose_name='Dirección de envio', help_text="Dirección de envio de la empresa")
    toro_cs_observation = models.TextField(max_length=40, verbose_name='Observaciones Dirección', help_text=" Observaciones con respecto a la Dirección de envio de la empresa")
    toro_cs_date_creation = models.DateField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación dirección')
    def __unicode__(self):
       return u'%s %s' %(self.toro_cs_date_creation, self.toro_cs)
        
    class Meta:
        ordering = ['toro_cs_date_creation']
        verbose_name = "Direcciónes de envio y despacho"

class Company(models.Model):
    toro_c_type_id = models.IntegerField(max_length= 2, choices=((1, 'Cédula'),(2, 'NIT'),(3, 'Extranjería')), verbose_name='Tipo de identificación', help_text="Tipo de identificación de la empresa")
    toro_c_id = models.CharField(max_length=20, verbose_name='Número identificación', help_text="Número de identificación de la empresa")
    toro_c_name = models.CharField(max_length=60, verbose_name='Nombre Empresa', help_text="Nombre de la empresa para prestarle el servicio")
    toro_c_phone = models.IntegerField(max_length=10, verbose_name='Telefono', help_text="Número telefonico de la empresa")
    toro_c_fax = models.IntegerField(max_length=10, verbose_name='FAX', help_text="Número telefonico del FAX de la empresa")
    toro_c_address = models.CharField(max_length=40, verbose_name='Dirección', help_text="Dirección de contacto de la empresa")
    toro_c_address_shipping = models.ManyToManyField(CompanyShipping)
    toro_c_city = models.ForeignKey(CodeDANE, verbose_name='Ciudad',  help_text='Código de la ciudad según el DANE')
    toro_c_number_authorized = models.CharField(max_length=40, verbose_name='Número Ministerio', help_text="Numero de autorización de la empresa según el Ministerio de Transporte")
    toro_c_date_creation = models.DateField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación empresa')
    def __unicode__(self):
       return u'%s %s %s %s' %(self.toro_c_id, self.toro_c_name, self.toro_c_city, self.toro_c_phone)
        
    class Meta:
        ordering = ['toro_c_date_creation']
        verbose_name = "Compañia"