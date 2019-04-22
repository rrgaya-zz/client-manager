from django.urls import path
from .views import person_list
from .views import person_new
from .views import person_update
from .views import person_delete

urlpatterns = [
    path('', person_list, name='person_list'),
    path('list/', person_list, name='person_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:id>/', person_update, name='person_update'),
    path('delete/<int:id>/', person_delete, name='person_delete'),
]