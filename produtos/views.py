from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework import generics
from django.shortcuts import render


class ProdutoApi(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


def product_list(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/produtos.html", {"produtos": produtos})