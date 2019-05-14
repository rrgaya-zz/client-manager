from django.db import models
from clientes.models import Person
from produtos.models import Produto
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Venda(models.Model):

    numero = models.CharField(max_length=5)
    valor = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=50, decimal_places=2)
    impostos = models.DecimalField(max_digits=50, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    def __str__(self):
        return self.numero


    # def get_total(self):
    #     total = 0
    #     for produto in self.produtos.all():
    #         total += produto.preco
    #
    #     return (total - self.desconto) - self.impostos

class ItensDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()  # Isso esta em float para por hora pois ainda nao tem fato de conversão
    desconto = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
        return self.venda.numero + " - " + self.produto.descricao


# TODO: Signal p/ refatorar
# @receiver(m2m_changed, sender=Venda.produtos.through)
def update_vendas_total(sender, instance, **kwargs):
    instance.valor = instance.get_total()
    instance.save()

    # FIXME: Solução usando post_save
    # total = instance.get_total()
    # Venda.objects.filter(id=instance.id).update(total=total)

