from cloudinary.models import CloudinaryField
from django.db import models
from django.conf import settings


class TimestampClass(models.Model):
    created = models.DateTimeField("criado em", auto_now_add=True, auto_now=False)
    modified = models.DateTimeField("modificado em", auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc

    class Meta:
        verbose_name = "Doc"
        verbose_name_plural = "Doc"


class Person(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE
    )
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

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def nome_completo(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        permissions = (("deletar_clientes", "DELETAR CLIENTES"),)
        unique_together = (("first_name", "telefone"),)
