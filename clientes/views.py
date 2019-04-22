from django.shortcuts import render, redirect, get_list_or_404
from .models import Person
from .forms import PersonForm

from django.contrib.auth.decorators import login_required


@login_required()
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {"persons": persons})


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