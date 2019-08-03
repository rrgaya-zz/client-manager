from django.urls import path
from .views import ProdutoApi


urlpatterns = [
    path('api/', ProdutoApi.as_view(), name='produto_apu'),
]