from rest_framework import serializers
from .models import TestDafiti


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDafiti
        fields = ('id', 'url', 'produto', 'quantidade', 'valor', 'estoque_valor')
        read_only_fields = ('estoque_valor', )