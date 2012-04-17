# -*- coding: utf-8 -*-
from django.utils import unittest
from django.test import TestCase
from django.db import IntegrityError
from city.models import CodeDANE
from datetime import datetime
"""
    toro_cd_id_city = models.IntegerField(max_length=10, verbose_name='Código Ciudad', help_text="Código de identificación de la ciudad según DANE", unique=True)
    toro_cd_name_city = models.CharField(max_length=20, verbose_name='Nombre Ciudad', help_text="Nombre de la ciudad, municipio, cacerio según DANE")
    toro_cd_dpto = models.CharField(max_length=20, verbose_name='Nombre Departamento', help_text="Nombre de identificación de la ciudad según DANE")
"""
class CodeDANETestCase(TestCase):
    """" Test sobre los Metodos de guardado """
    id_city = 11001
    name_city = "Bogotá"
    dpto = "Bogota D.C."
    
    def setUp(self):
        self.bogota = CodeDANE.objects.create(toro_cd_id_city=self.id_city,
                                              toro_cd_name_city= self.name_city,
                                              toro_cd_dpto= self.dpto)

        
    def test_model(self):
        self.assertAlmostEqual(self.bogota.toro_cd_id_city, self.id_city)
