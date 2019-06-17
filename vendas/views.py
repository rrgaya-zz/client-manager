from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from .models import Venda, ItemDoPedido
from .form import ItemPedidoForm



class DashboardView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("vendas.ver_dashboard"):
            return HttpResponse("Acesso negado")

        return super(DashboardView, self).dispatch(request, *args, **kwargs)


    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desc()
        data['soma'] = Venda.objects.soma()
        data['qt_vendas'] = Venda.objects.qt_vendas()
        data['tm_max'] = Venda.objects.tm_max()
        data['tm_min'] = Venda.objects.tm_min()
        data['num_ped_nfe'] = Venda.objects.num_ped()

        return render(request, 'vendas/dash.html', data)


class Novo_pedido(View):
    def get(self, request):
        return render(request, "vendas/novo-pedido.html")

    def post(self, request):
        data = {}
        data['form_item'] = ItemPedidoForm()
        data['numero'] = request.POST['numero']
        data['desconto'] = float(request.POST['desconto'].replace(',', '.'))
        data['venda_id'] = request.POST['venda_id']

        if data['venda_id']:
            venda = Venda.objects.get(id=data['venda_id'])
            venda.desconto = data['desconto']
            venda.numero = data['numero']
            venda.save()
        else:
            venda = Venda.objects.create(
                numero = data['numero'], desconto = data['desconto'])

        itens = venda.itemdopedido_set.all()
        data['venda'] = venda
        data['itens'] = itens

        return render(request, "vendas/novo-pedido.html", data)


class NovoItemPedido(View):
    def get(self, request, pk):
        pass

    def post(self, request, venda):
        data = {}
        item = ItemDoPedido.objects.create(
            produto_id=request.POST['produto_id'],
            quantidade=request.POST['quantidade'],
            desconto=request.POST['desconto'],
            venda_id=venda
        )
        data['item'] = item
        data['form_item'] = ItemPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda
        data['itens'] = item.venda.itemdopedido_set.all()

        return render(request, "vendas/novo-pedido.html", data)


class ListaVendas(View):
    def get(self, request):
        vendas = Venda.objects.all()
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas})


class EditPedido(View):
    def get(self, request, venda):
        data = {}
        venda = Venda.objects.get(pk=venda)
        data['form_item'] = ItemPedidoForm()
        data['numero'] = venda.numero
        data['desconto'] = float(venda.desconto)
        data['venda'] = venda
        data['itens'] = venda.itemdopedido_set.all()
        return render(request, "vendas/novo-pedido.html", data)
