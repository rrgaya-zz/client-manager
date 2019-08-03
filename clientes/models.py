from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class TimestampClass(models.Model):
    created = models.DateTimeField("criado em", auto_now_add=True, auto_now=False)
    modified = models.DateTimeField("modificado em", auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=50, decimal_places=2)
    bio = models.TextField()
    photo = CloudinaryField("imagem")
    doc = models.OneToOneField(
        Documento, null=True, blank=True, on_delete=models.CASCADE
    )
    telefone = models.CharField(max_length=20, null=True, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def nome_completo(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        permissions = (("deletar_clientes", "DELETAR CLIENTES"),)

        unique_together = (("first_name", "telefone"),)
