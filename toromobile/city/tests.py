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

#Inegrity in unicode
class  CodeDANEUnicodeTest(TestCase):
    def testUnicode(self):
        id_city = 13212
        name_city = u'Córdoba'
        dpto_city = u'Bolívar'
        s = CodeDANE.objects.create(toro_cd_id_city=id_city, toro_cd_name_city=name_city, toro_cd_dpto=dpto_city)
        self.assertEqual(unicode(s), u'13212 Córdoba Bolívar')
"""             
    def tearDown(self):
        'Depopulate created model instances from test database.'
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
                
        self.assertEqual(CodeDANE.objects.all().count(), 0)
"""
#fixtures
class CodeDANEFixtures(TestCase):
    fixtures = ['../city/fixtures/test_codedane.json']
    
    def testCodeDADE(self):
        q = CodeDANE.objects.all().filter(toro_cd_id_city=63212)
        self.assertEqual(q.count(), 1)