from django.urls import path
from .views import home
from .views import meu_logout

urlpatterns = [
    path('', home, name='home'),
    path('logout', meu_logout, name='meu_logout')
]