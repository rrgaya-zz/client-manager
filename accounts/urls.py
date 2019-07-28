from django.urls import path
from .views import SingUp


urlpatterns = [
    path('register/', SingUp.as_view(), name="SingUp")
]