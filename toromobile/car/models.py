# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, time
from city.models import CodeDANE
"""
    Este modelo se hace con base a la documento del Ministerio de Trasporte
    Direccion de transito y transporte, Sistema de Información para la generación del
    Manifiesto de Cargas "SIMCA".
    El siguiente modelo hace referencia a "Archivo plano maestro de vehiculo"
"""
#Tipo de Carroceria de los Carros referente a MINMTICARROC
class CarBodyWork(models.Model):
    toro_cbw_code = models.IntegerField(max_length=3, verbose_name='Código', help_text="Código correspondiente a la carroceria")
    toro_cbw_description = models.CharField(max_length=20, verbose_name='Descripción', help_text="Nombre completo del tipo de carroceria")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cbw_code, self.toro_cbw_description)
        
    class Meta:
        ordering = ['toro_cbw_code']
        verbose_name = "Tipos de Carroceria Vehiculo"

#Color de los carros referente MINMCOLP    
class CarColor(models.Model):
    toro_cc_code = models.IntegerField(max_length=4, verbose_name='Código', help_text="Código correspondiente del Color")
    toro_cc_description = models.CharField(max_length=20, verbose_name='Descripción', help_text="Nombre completo del Color")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cc_code, self.toro_cc_description)
        
    class Meta:
        ordering = ['toro_cc_code']
        verbose_name = "Tipos de Colores Vehiculo"

#Datos del encargado del Vehiculo    
class CarMandated(models.Model):
    toro_cm_type_id = models.IntegerField(max_length= 2, choices=((1, 'Cédula'),(2, 'NIT'),(3, 'Extranjería')), verbose_name='Tipo de identificación', help_text="Si el evento es Streaming o en Radio")
    toro_cm_id = models.CharField(max_length=20, verbose_name='Número identificación', help_text="Número de identificación del encargado del vehiculo")
    toro_cm_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Nombre Empresa', help_text="Nombre de la empresa propietaria si es necesario")
    toro_cm_first_name = models.CharField(max_length=32, verbose_name='Nombre(s)', help_text="Nombre(s) de la empresa o del encargado del vehiculo")
    toro_cm_last_name = models.CharField(max_length=32, verbose_name='Apellido(s)', help_text="Apellido(s) de la empresa o del encargado del vehiculo")
    #Optimización para ver en el admin site de Django
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_cm_id, self.toro_cm_first_name, self.toro_cm_last_name)
        
    class Meta:
        ordering = ['toro_cm_id']
        verbose_name = "Responsables Vehiculo"
            
#Marcas de los carros con referencia a MINMTIMA
class CarMark(models.Model):
    toro_cm_code = models.CharField(max_length=2, verbose_name='Código', help_text="Código de abreviación Marca de carro")
    toro_cm_description = models.CharField(max_length=60, verbose_name='Descripción', help_text="Nombre completo de la marca para describir el Carro")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cm_code, self.toro_cm_description)
        
    class Meta:
        ordering = ['toro_cm_code']
        verbose_name = "Marcas de los Vehiculo"

#Linea de los carros con su respectiva marca referente a MINMMARCA
class CarLine(models.Model):
    toro_cl_code = models.ForeignKey(CarMark)
    toro_cl_line = models.IntegerField(max_length=10, verbose_name='Linea', help_text="Número correspondiente a la linea de Carro")
    toro_cl_description = models.CharField(max_length=60, verbose_name='Descripción', help_text="Nombre completo de la linea de Carro")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cl_code, self.toro_cl_description)
        
    class Meta:
        ordering = ['toro_cl_code']
        verbose_name = "Tipo de Lineas Vehiculo"
#Datos del dueño del Vehiculo
class CarOwner(models.Model):
    toro_co_type_id = models.IntegerField(max_length= 2, choices=((1, 'Cédula'),(2, 'NIT'),(3, 'Extranjería')), verbose_name='Tipo de identificación', help_text="Tipo de identificación del propietario del vehiculo")
    toro_co_id = models.CharField(max_length=20, verbose_name='Número identificación', help_text="Número de identificación del dueño del vehiculo")
    toro_co_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Nombre Empresa', help_text="Nombre de la empresa propietaria si es necesario")
    toro_co_first_name = models.CharField(max_length=32, verbose_name='Nombre(s)', help_text="Nombre(s) de la empresa o del dueño del vehiculo")
    toro_co_last_name = models.CharField(max_length=32, verbose_name='Apellido(s)', help_text="Apellido(s) de la empresa o del dueño del vehiculo")
    toro_co_register_national = models.IntegerField(max_length= 20, verbose_name='Registro Nacional', help_text="Registro Nacional de Transporte de Carga Número")
    #Optimización para ver en el admin site de Django
    def __unicode__(self):
       return u'%s %s %s' %(self.toro_co_id, self.toro_co_first_name, self.toro_co_last_name)
        
    class Meta:
        ordering = ['toro_co_type_id']
        verbose_name = "Propietarios Vehiculo"

#Placa del Vehículo        
class CarPlate(models.Model):
    toro_cp_plate = models.CharField(max_length=6, verbose_name='Placa Vehiculo', help_text="Tres letras y tres número ABC123 Sin espacios")
    toro_cp_plate_city = models.ForeignKey(CodeDANE, verbose_name='Ciudad Placa', help_text="Ciudad de registro de la Placa")
    def __unicode__(self):
       return u'%s %s' %(self.toro_cp_plate, self.toro_cp_plate_city)
        
    class Meta:
        ordering = ['toro_cp_plate']
        verbose_name = "Placa Vehículo"        
#Configuración del Remolque
class CarTrailer(models.Model):
    toro_ct_id = models.CharField(max_length=60, verbose_name='Designación', help_text="designación de acuerdo con la disposición de los ejes")
    toro_ct_description = models.CharField(max_length=60, verbose_name='Descripción', help_text="Caracteristicas de la designación del remolque")
    toro_ct_scheme = models.ImageField(verbose_name='Esquema', help_text="Imagen Referente al Esquema del Tipo de Carro", upload_to='uploads')
    def __unicode__(self):
       return u'%s %s' %(self.toro_ct_id, self.toro_ct_description)
        
    class Meta:
        ordering = ['toro_ct_id']
        verbose_name = "Configuración Remolque"


#Clase general para crear el carro
class Car(models.Model):
   toro_car_plate = models.ForeignKey(CarPlate, verbose_name='Placa Vehículo', help_text="Placa del Vehiculo a Usar")
   toro_car_mark = models.ForeignKey(CarMark, verbose_name='Marca Vehiculo', help_text="Marca del Vehículo")
   toro_car_line = models.ForeignKey(CarLine, verbose_name='Linea Vehiculo', help_text="Linea según Marca del Vehículo")
   toro_car_model_year =  models.DateField(verbose_name='Modelo', help_text="Ingrese el Modelo del año de producción del Carro Ejemplo: 2001")
   toro_car_model_power = models.DateField(blank=True, null=True, verbose_name='Modelo Repotenciado', help_text="año a que haya sido repotenciado o transformado un vehículo")
   toro_car_num_serial = models.CharField(max_length=25, verbose_name='Número Serie', help_text="Número de serie del Vehiculo")
   toro_car_color = models.ForeignKey(CarColor, verbose_name='Color Vehiculo')
   toro_car_bodyWork = models.ForeignKey(CarBodyWork, verbose_name='Tipo de Carroceria')
   toro_car_trailer = models.ForeignKey(CarTrailer, blank=True, verbose_name='Configuración')
   toro_car_kilo = models.FloatField(max_length=5, verbose_name='Peso (Kg.)', help_text="Peso del vehiculo vacio en Kilogramos(Kg.)")
   toro_car_register = models.IntegerField(max_length=8, verbose_name='Registro Nacional', help_text="Registro Nacional de Transporte de Carga Número")
   toro_car_soat = models.CharField(max_length=20, verbose_name='S.O.A.T', help_text="Número de poliza del S.O.A.T")
   toro_car_id_insurance = models.IntegerField(max_length=11, verbose_name='NIT Aseguradora', help_text="Número de identificación de la aseguradora")
   toro_car_soat_date = models.DateField(verbose_name='Fecha Vencimiento S.O.A.T', help_text="Fecha de vencimiento de la Poliza ")
   toro_car_owner = models.ForeignKey(CarOwner, verbose_name='Dueño Vehiculo')
   toro_car_mandated = models.ForeignKey(CarMandated, verbose_name='Responsable Vehiculo')
   toro_car_date_created = models.DateField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación vehiculo')
   #Optimización para ver en el admin site de Django
   def __unicode__(self):
       return u'%s %s' %(self.toro_car_plate, self.toro_car_date_created)
        
   class Meta:
        ordering = ['toro_car_plate']
        verbose_name = "Vehiculo"