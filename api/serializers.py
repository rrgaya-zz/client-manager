from rest_framework import serializers
from produtos.models import Produto


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'url', 'descricao', 'preco')