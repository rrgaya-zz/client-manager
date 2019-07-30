from django.core.checks import messages
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Person
from produtos.models import Produto
from vendas.models import Venda
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import logging
import csv, io
from rest_framework import viewsets
from .serializers import PersonSerializer
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView


logger = logging.getLogger("django")


@login_required()
def person_list(request):
    # nome = request.GET.get('nome', None)
    # sobrenome = request.GET.get('sobrenome', None)

    """BUSCA - nome && sobrenome -- nome OR sobrenome
    """
    # if nome or sobrenome:
    #     # persons = Person.objects.filter(first_name__icontains=nome, last_name__icontains=sobrenome)
    #     persons = Person.objects.filter(first_name__icontains=nome) | Person.objects.filter(last_name__icontains=sobrenome)
    # else:
    #     persons = Person.objects.all()
    persons = Person.objects.all()
    # persons = Person.objects.filter(id=1000)
    footer_menssage = "Desenvolvimento em Django 2.x"
    return render(request, 'person.html', {"persons": persons, "footer_menssage": footer_menssage})


@login_required()
def person_new(request):
    # TODO: Validar permissões
    # if not request.user.has_perm('clientes.add_person'):
    #     return HttpResponse("Nao autorizado")
    # elif not request.user.is_superuser():
    #     return HttpResponse("Não é superuser")
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
        # return person_list(request)

    return render(request, 'person_form.html', {'form': form})


@login_required()
def person_update(request, id):
    person = Person.objects.get(pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required()
def person_delete(request, id):
    person = Person.objects.get(pk=id)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person': person})


class PersonList(LoginRequiredMixin, ListView):
    model = Person
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        primeiro_acesso = self.request.session.get('prmeiro_acesso', False)
        if not primeiro_acesso:
            context['message'] = "Prmeiro acesso"
            self.request.session['prmeiro_acesso'] = True
        else:
            context['message'] = "Segundo acesso"
        print(context['message']) # Apenas em development
        return context


class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person
    """ Fazendo Override do metodo nativo do Django
        Diminuindo de 9 queries para 8
    """
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(
            pessoa_id=self.object.id
        )
        return context


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    # success_url = '/clientes/person_list/'
    success_url = reverse_lazy('person_list_cbv')


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    # success_url = '/clientes/person_list/'
    success_url = reverse_lazy('person_list_cbv')


class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ("clientes.deletar_clientes",)
    model = Person
    # success_url = reverse_lazy('person_list_cbv')
    def get_success_url(self):
        return reverse_lazy('person_list_cbv')


class ProdutoBulk(View):
    def get(self, request):
        produtos = ['notebook', 'mouse', 'teclado', 'monitor', 'HD', 'livros']
        list_produtos = []
        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)
        Produto.objects.bulk_create(list_produtos)
        return HttpResponse("Funcionou o BULK")


def api(request):
    produto = Produto.objects.last()
    response = model_to_dict(produto)

    produtos = Produto.objects.all()
    lista_produtos = []

    for p in produtos:
        lista_produtos.append(model_to_dict(p))

    return JsonResponse(lista_produtos, safe=False, status=200)


class APICBV(View):
    def get(self, request):
        data = {'nome': 'Ricardo', 'bio': "Software Engineer"}
        produtos = Produto.objects.all()
        lista_produtos = []

        for p in produtos:
            lista_produtos.append(model_to_dict(p))

        return JsonResponse(lista_produtos, safe=False)


def csv_download(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response


def clientes_upload(request):
    template_name = "clientes/upload.html"
    prompt = {
        'Ordem': 'first_name, last_name, age, salary, bio'
    }

    if request.method == "GET":
        return render(request, template_name, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Esta file não é csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Person.objects.update_or_create(
            first_name=column[0],
            last_name=column[1],
            age=column[2],
            salary=column[3],
            bio=column[4],
        )
    context = {}
    return render(request, template_name, context)


# class PersonViewSet(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonViewAPI(APIView):
    def get(self, request):
        person = Person.objects.all()
        return Response({"pessoas": person})