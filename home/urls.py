from django.urls import path
from .views import home
from .views import meu_logout
from .views import HomePageView
from .views import MyView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name='home'),
    path('logout', meu_logout, name='meu_logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html'), name='test'),
    path('home3/', HomePageView.as_view(), name='test2'),
    path('view/', MyView.as_view(), name='test3'),
]