from django.urls import path
from .views import Signup


urlpatterns = [
    path('criar/', Signup.as_view(), name="signup")
]