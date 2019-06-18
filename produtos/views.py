from django.shortcuts import render
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework import generics


class ProdutoApi(generics.ListAPIView):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer