from django.db import models
from django.db.models import Sum, F, FloatField, Max
from clientes.models import Person
from produtos.models import Produto
from django.db.models.signals import post_save
from django.dispatch import receiver


class Venda(models.Model):

    numero = models.CharField(max_length=5)
    valor = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    def __str__(self):
        return self.numero

    # TODO: Refactoring necessary
    def calcular_total(self):
        tot = self.itemdopedido_set.all().aggregate(
            tot_ped=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_ped'] or 0

        tot = tot - (float(self.impostos) + float(self.desconto))
        self.valor = tot
        Venda.objects.filter(id=self.id).update(valor=tot)


class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()  # Isso esta em float para por hora pois ainda nao tem fato de conversão
    desconto = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return self.venda.numero + " - " + self.produto.descricao



"""Usando Signals
"""
# @receiver(m2m_changed, sender=Venda.produtos.through)
# def update_vendas_total(sender, instance, **kwargs):
#     instance.valor = instance.calcular_total()
#     instance.save()


@receiver(post_save, sender=ItemDoPedido)
def update_vendas_total(sender, instance, **kwargs):
    instance.venda.calcular_total()

@receiver(post_save, sender=Venda)
def update_vendas_total2(sender, instance, **kwargs):
    instance.calcular_total()