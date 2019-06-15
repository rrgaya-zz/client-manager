from django.db import models
from django.db.models import Avg, Max, Min, Count, Sum

class VendaManager(models.Manager):

    def media(self):
        return self.all().aggregate(Avg('valor'))['valor__avg']

    def media_desc(self):
        return self.all().aggregate(Avg("desconto"))['desconto__avg']

    def soma(self):
        return self.all().aggregate(Sum("valor"))['valor__sum']

    def qt_vendas(self):
        return self.all().aggregate(Count("id"))['id__count']

    def tm_max(self):
        return self.all().aggregate(Max("valor"))['valor__max']

    def tm_min(self):
        return self.all().aggregate(Min("valor"))['valor__min']

    def num_ped(self):
        return self.filter(nfe_emitida=True).aggregate(Count("id"))['id__count']