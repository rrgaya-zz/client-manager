from django.urls import path
from .views import ProdutoApi


urlpatterns = [
    # path('', person_list, name='person_list'),
    path('api/', ProdutoApi.as_view(), name='produto_apu'),

]