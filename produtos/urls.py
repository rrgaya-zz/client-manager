from django.urls import path
from .views import ProdutoApi, product_list


urlpatterns = [
    path('', product_list, name='product_list'),
    path('api/', ProdutoApi.as_view(), name='produto_apu'),
]