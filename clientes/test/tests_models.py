# coding=utf-8

from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from clientes.models import Person



class TestRecord(TestCase):

    def setUp(self):
        self.pessoa = mommy.make(Person, name='Person Test')

    def test_record_creation(self):
        self.assertTrue(isinstance(self.pessoa, Person))
        self.assertEquals(self.record.__str__(), self.pessoa.name)