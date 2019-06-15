from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from .models import Venda



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