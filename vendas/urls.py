from django.urls import path
from .views import DashboardView, Novo_pedido, NovoItemPedido


urlpatterns = [
    path('novo-pedido/', Novo_pedido.as_view(), name='novo_pedido'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('novo-item-pedido/<int:venda>', NovoItemPedido.as_view(), name='novo-item-pedido'),
]