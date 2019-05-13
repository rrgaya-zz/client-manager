from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404
from .models import Person, Produto, Venda
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
# Import para CBV
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic import View

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
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
        # return person_list(request)

    return render(request, 'person_form.html', {'form': form})


@login_required()
def person_update(request, id):
    # person = get_list_or_404(Person, pk=id)
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


class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
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


class PersonCreate(CreateView):

    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    # success_url = '/clientes/person_list/'
    success_url = reverse_lazy('person_list_cbv')


class PersonUpdate(UpdateView):

    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    # success_url = '/clientes/person_list/'
    success_url = reverse_lazy('person_list_cbv')


class PersonDelete(DeleteView):
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
