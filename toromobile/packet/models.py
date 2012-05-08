# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from city.models import CodeDANE

"""
    Este modelo se hace con base a la documento del Ministerio de Trasporte
    Direccion de transito y transporte, Sistema de Información para la generación del
    Manifiesto de Cargas "SIMCA".
    El siguiente modelo hace referencia a "Archivo plano maestro de mercancias"
"""
#Modelos con respecto a la Codificación de los Productos con base a MINMPRODUCT
class PackageProduct(models.Model):
    toro_pp_id = models.IntegerField(max_length=10, verbose_name='Código Producto', help_text="Código Referente al Producto")
    toro_pp_description = models.TextField(max_length=300, verbose_name='Descripción Producto', help_text="Descripción Referente al Producto")
    def __unicode__(self):
       return u'%s %s' %(self.toro_pp_id, self.toro_pp_description)
        
    class Meta:
        ordering = ['toro_pp_id']
        verbose_name = "Código Producto"

class Package(models.Model):
    toro_p_manifest = models.CharField(max_length=14, verbose_name='Número Manifiesto', help_text="Número de manifiesto expedido por el Ministerio de Transporte")
    toro_p_remittance = models.CharField(max_length=10, verbose_name='Número Remesa', help_text="Número de la remesa según Ministerio de Transporte")
    toro_p_measuring_unit = models.IntegerField(max_length=2, choices = ((1,'Kilogramos'), (2, 'Galones')),verbose_name='Unidad Medida', help_text="Unidad de medida según manifiesto de carga")
    toro_p_amount = models.FloatField(max_length=5, verbose_name='Cantidad', help_text="Cantidad diferente de cero(0) si unidad de medida es galones o Kilogramos")
    toro_p_peso = models.FloatField(max_length=5, verbose_name='Cantidad', help_text="Peso total de todas los productos, expresado en toneladas")
    toro_p_unit = models.IntegerField(max_length=2, choices = (
        #Se aplica al transporte de vehículos y maquinaria
        (-1, 'No Aplica N.A.'),
        (-2, 'Varios'),
        (-3, 'Granel Solido'),
        (-4, 'Rollos'),
        (-5, 'Garrafones'),
        (-6, 'Cilindros'),
        (-7, 'Bolsas'),
        (-8, 'Guacales'),
        (0, 'Paquete'),
        (1,'Caja'),
        (2, 'Bidón'),
        (3, 'Saco'),
        (4, 'Bulto'),
        (5, 'Tonel'),
        (6, 'Granel Liquido'),
        (7, 'Un Contenedor de 20 Pies'),
        (8, 'Dos Contenedores de 20 Pies'),
        (9, 'Un Contenedor de 40 Pies')), verbose_name='Unidad Empaque', help_text="Unidad de Empaque según manifiesto de carga")
    toro_p_nature = models.IntegerField(max_length=2, choices = (
        (1, 'Carga Normal'),
        (2, 'Carga Peligrosa'),
        (3, 'Carga Extradimendionada'),
        (4, 'Carga Extrapesada')), verbose_name='Naturaleza Carga', help_text="Naturaleza de la Carga según manifiesto de carga")
    toro_p_product = models.ManyToManyField(PackageProduct, verbose_name='producto(s)')
    """
        Tipo de servicios prestados por toromobile
        Directo : visualizará las remesas para el destino final
        Reguero: visualizará las remesas que hay entre el origen y el destino
        Masiva: este servicio omite el valor del flete fijo si la ruta seleccionada posee
        este valor y toma el valor del flete de la remesa
    """
    toro_p_service = models.IntegerField(max_length=1, choices=((1,'Directo'),(2, 'Reguero'), (3, 'Masiva') ), verbose_name='Tipo Servicio', help_text="Tipo de Servicio")
    toro_p_description = models.TextField(max_length=200, verbose_name='Descripción Abreviada', help_text="Descripción abreviada de Producto(s)")
    toro_p_name_shipping = models.CharField(max_length=120, verbose_name='Persona Remitente', help_text="Nombre de la persona que remite Apellido Nombre")
    toro_p_name_receiver = models.CharField(max_length=120, verbose_name='Persona Destinatario', help_text="Nombre de la persona que recibe Apellido Nombre")
    toro_p_city_receiver = models.ForeignKey(CodeDANE, verbose_name='Dirección Destino', help_text="Código de Ciudad según DANE")
    toro_p_date_creation = models.DateField(default=datetime.now, auto_now = False, editable=False, verbose_name='Fecha de creación de paquete')
    #Optimización para el admin
    def __unicode__(self):
       return u'%s %s %s %s' %(self.toro_p_manifest, self.toro_p_name_shipping, self.toro_p_name_receiver, self.toro_p_city_receiver)
        
    class Meta:
        ordering = ['toro_p_date_creation']
        verbose_name = "Paquete"