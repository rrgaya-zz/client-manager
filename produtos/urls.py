from django.urls import path
from .views import ProdutoApi, ProductList


urlpatterns = [
    path('', ProductList, name='person_list'),
    path('api/', ProdutoApi.as_view(), name='produto_apu'),

]