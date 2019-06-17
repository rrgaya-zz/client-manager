from django import forms
from .models import ItemDoPedido


class ItemPedidoForm(forms.Form):
    produto_id = forms.CharField(label="ID DO PRODUTO", max_length=100)
    quantidade = forms.IntegerField(label="QUANTIDADE")
    desconto = forms.DecimalField(label="DESCONTO", max_digits=7, decimal_places=2)


class ItemDoPedidoModelForm(forms.ModelForm):
    class Meta:
        model = ItemDoPedido
        fields = ['desconto', 'quantidade']