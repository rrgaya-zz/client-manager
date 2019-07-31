from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class Signup(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    success_message = "Usuário cadastrado"