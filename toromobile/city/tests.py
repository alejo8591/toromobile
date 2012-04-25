# -*- coding: utf-8 -*-
from django.utils import unittest
from django.test import TestCase
from django.db import IntegrityError
from city.models import CodeDANE
from datetime import datetime
from django.conf import Settings


"""
    Data struct in models city
    toro_cd_id_city :  int
    toro_cd_name_city : string
    toro_cd_dpto : string
"""
MODELS= [CodeDANE]

#Integrity in data
class CondeDANEIntegrity(TestCase):
    def setUp(self):
        self.id_city = [15212, 52215]
        self.name_city = [u'COPER', u'CORDOBA']
        self.dpto_city = [u'BOYACÁ', u'NARIÑO']
        
    def integrity(self): 
           print CodeDANE.objects.create(toro_cd_id_city=self.id_city[0], toro_cd_name_city= self.name_city[0], toro_cd_dpto =self.dpto_city[0])
            
    def tearDown(self):
        'Depopulate created model instances from test database.'
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
                
        self.assertEqual(CodeDANE.objects.all().count(), 0)
        
    
#Inegrity in unicode
class  CodeDANEUnicodeTest(TestCase):
    def testUnicode(self):
        id_city = 13212
        name_city = u'Córdoba'
        dpto_city = u'Bolívar'
        s = CodeDANE.objects.create(toro_cd_id_city=id_city, toro_cd_name_city=name_city, toro_cd_dpto=dpto_city)
        self.assertEqual(unicode(s), u'13212 CÓRDOBA BOLÍVAR')
             
    def tearDown(self):
        'Depopulate created model instances from test database.'
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
                
        self.assertEqual(CodeDANE.objects.all().count(), 0)

#fixtures
class CodeDANEFixtures(TestCase):
    #python manage.py dumpdata city --indent 4 > city/fixtures/test_codedane.json
     
    fixtures = ['test_codedane.json']
    
    def testCodeDANE(self):
        q = CodeDANE.objects.filter(pk=1, toro_cd_id_city=3222)
        self.assertEqual(q.count(), 1)