from django.urls import path
from .views import DashboardView, Novo_pedido, NovoItemPedido, ListaVendas,EditPedido, DeletePedido


urlpatterns = [
    path('', ListaVendas.as_view(), name='lista_vendas'),
    path('novo-pedido/', Novo_pedido.as_view(), name='novo_pedido'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('novo-item-pedido/<int:venda>', NovoItemPedido.as_view(), name='novo-item-pedido'),
    path('edit-pedido/<int:venda>', EditPedido.as_view(), name='edit_pedido'),
    path('delete-pedido/<int:venda>', DeletePedido.as_view(), name='delete_pedido'),
]