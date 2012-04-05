# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, time
"""
    Este modelo se hace con base a la documento del Ministerio de Trasporte
    Direccion de transito y transporte, Sistema de Información para la generación del
    Manifiesto de Cargas "SIMCA".
    El siguiente modelo hace referencia a "Archivo plano maestro de vehiculo"
"""
#Marcas de los carros con referencia a MINMTIMA
class CarMark(models.Model):
    toro_cm_code = models.CharField(max_length=2, verbose_name='Código', help_text="Código de abreviación Marca de carro")
    toro_cm_description = models.CharField(max_length=60, verbose_name='Descripción', help_text="Nombre completo de la marca para describir el Carro")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cm_code, self.toro_cm_code)
        
    class Meta:
        ordering = ['toro_cm_code']

#Linea de los carros con su respectiva marca referente a MINMMARCA
class CarLine(models.Model):
    toro_cl_code = models.ForeignKey(CarMark)
    toro_cl_line = models.IntegerField(max_length=10, verbose_name='Linea', help_text="Número correspondiente a la linea de Carro")
    toro_cl_description = models.CharField(max_length=60, verbose_name='Descripción', help_text="Nombre completo de la linea de Carro")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cl_code, self.toro_cl_description)
        
    class Meta:
        ordering = ['toro_cl_code']
    
#Color de los carros referente MINMCOLP    
class CarColor(models.Model):
    toro_cc_code = models.IntegerField(max_length=4, verbose_name='Código', help_text="Código correspondiente del Color")
    toro_cc_description = models.CharField(max_length=20, verbose_name='Descripción', help_text="Nombre completo del Color")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cc_code, self.toro_cc_description)
        
    class Meta:
        ordering = ['toro_cc_code']
    
#Tipo de Carroceria de los Carros referente a MINMTICARROC
class CarBodyWork(models.Model):
    toro_cbw_code = models.IntegerField(max_length=3, verbose_name='Código', help_text="Código correspondiente a la carroceria")
    toro_cbw_description = models.CharField(max_length=20, verbose_name='Descripción', help_text="Nombre completo del tipo de carroceria")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cbw_code, self.toro_cbw_description)
        
    class Meta:
        ordering = ['toro_cbw_code']
        
#Datos del dueño del Vehiculo
class CarOwner(models.Model):
    toro_co_type_id = models.IntegerField(max_length= 2, choices=((1, 'Cédula'),(2, 'NIT'),(3, 'Extranjería')), verbose_name='Tipo de identificación', help_text="Si el evento es Streaming o en Radio")
    toro_co_owner_id = models.CharField(max_length=20, verbose_name='Número identificación', help_text="Número de identificación del dueño del vehiculo")
    toro_co_owner_first_name = models.CharField(max_length=32, verbose_name='Nombre(s)', help_text="Nombre(s) de la empresa o del dueño del vehiculo")
    toro_co_owner_last_name = models.CharField(max_length=32, verbose_name='Apellido(s)', help_text="Apellido(s) de la empresa o del dueño del vehiculo")
    #Optimización para ver en el admin site de Django
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_co_type_id, self.toro_co_owner_first_name, self.toro_co_owner_last_name)
        
    class Meta:
        ordering = ['toro_co_type_id']
        
#Datos del encargado del Vehiculo    
class CarMandated(models.Model):
    toro_cm_type_id = models.IntegerField(max_length= 2, choices=((1, 'Cédula'),(2, 'NIT'),(3, 'Extranjería')), verbose_name='Tipo de identificación', help_text="Si el evento es Streaming o en Radio")
    toro_cm_owner_id = models.CharField(max_length=20, verbose_name='Número identificación', help_text="Número de identificación del encargado del vehiculo")
    toro_cm_owner_first_name = models.CharField(max_length=32, verbose_name='Nombre(s)', help_text="Nombre(s) de la empresa o del encargado del vehiculo")
    toro_cm_owner_last_name = models.CharField(max_length=32, verbose_name='Apellido(s)', help_text="Apellido(s) de la empresa o del encargado del vehiculo")
    #Optimización para ver en el admin site de Django
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_cm_type_id, self.toro_cm_owner_first_name, self.toro_cm_owner_last_name)
        
    class Meta:
        ordering = ['toro_cm_type_id']
        
#Clase general para crear el carro
class Car(models.Model):
   toro_car_plate = models.CharField(max_length=6, verbose_name='Placa Vehiculo', help_text="Tres letras y tres número ABC123 Sin espacios")
   toro_car_mark = models.ForeignKey(CarMark, verbose_name='Marca Vehiculo')
   toro_car_line = models.ForeignKey(CarLine, verbose_name='Linea Vehiculo')
   toro_car_model_year =  models.DateField(verbose_name='Modelo', help_text="Ingrese el Modelo del año de producción del Carro Ejemplo: 2001")
   toro_car_model_power = models.DateField(verbose_name='Modelo Repotenciado', help_text="año a que haya sido repotenciado o transformado un vehículo", blank=True)
   toro_car_num_serial = models.CharField(max_length=25, verbose_name='Número Serie', help_text="Número de serie del Vehiculo")
   toro_car_color = models.ForeignKey(CarColor, verbose_name='Color Vehiculo')
   toro_car_bodyWork = models.ForeignKey(CarBodyWork, verbose_name='Tipo de Carroceria')
   toro_car_kilo = models.FloatField(max_length=5, verbose_name='Peso (Kg.)', help_text="Peso del vehiculo vacio en Kilogramos(Kg.)")
   toro_car_register = models.IntegerField(max_length=8, verbose_name='Registro Nacional', help_text="Número de registro Nacional del Vehiculo")
   toro_car_soat = models.CharField(max_length=20, verbose_name='S.O.A.T', help_text="Número de poliza del S.O.A.T")
   toro_car_id_insurance = models.IntegerField(max_length=11, verbose_name='NIT Aseguradora', help_text="Número de identificación de la aseguradora")
   toro_car_soat_date = models.DateField(verbose_name='Fecha Vencimiento S.O.A.T', help_text="Fecha de vencimiento de la Poliza ")
   toro_car_owner = models.ForeignKey(CarOwner, verbose_name='Dueño Vehiculo')
   toro_car_mandated = models.ForeignKey(CarMandated, verbose_name='Tenedor Vehiculo')
   toro_date_car_created = models.DateField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación vehiculo')
   #Optimización para ver en el admin site de Django
   def __unicode__(self):
       return u'%s %s' %(self.toro_car_plate, self.toro_date_car_created)
        
   class Meta:
        ordering = ['toro_car_plate']