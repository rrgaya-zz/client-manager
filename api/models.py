from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TestDafiti(models.Model):
    gender_status = (
        ('M', 'Masculina'),
        ('F', 'Feminina'),
    )
    product_id = models.IntegerField(null=True, blank=True)
    product = models.CharField(max_length=20)
    quantity = models.IntegerField()
    cost_price = models.DecimalField(decimal_places=2, max_digits=20)
    markup = models.DecimalField(decimal_places=2, max_digits=20)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    category = models.CharField(max_length=100)
    gender = models.CharField(choices=gender_status, max_length=2)
    stock_value = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True, default=0)

    class Meta:
        unique_together = ('product_id', 'product', 'quantity', )

    def __str__(self):
        return self.product

    def get_valor(self):
        total = self.quantity * self.price
        self.estoque_valor = total
        TestDafiti.objects.filter(id=self.id).update(estoque_valor=total)


@receiver(post_save, sender=TestDafiti)
def update_vendas_total2(sender, instance, **kwargs):
    instance.get_valor()