from django.urls import path
from .views import DashboardView, Novo_pedido


urlpatterns = [
    path('novo-pedido/', Novo_pedido.as_view(), name='novo-pedido'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]