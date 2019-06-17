from django.urls import path
from .views import person_list
from .views import person_new
from .views import person_update
from .views import person_delete
from .views import PersonList
from .views import PersonDetail
from .views import PersonCreate
from .views import PersonUpdate
from .views import PersonDelete
from .views import ProdutoBulk
from .views import api
from .views import APICBV


urlpatterns = [
    path('', person_list, name='person_list'),
    path('list/', person_list, name='person_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:id>/', person_update, name='person_update'),
    path('delete/<int:id>/', person_delete, name='person_delete'),
    path('person_list/', PersonList.as_view(), name='person_list_cbv'),
    path('person_detail/<int:pk>/', PersonDetail.as_view(), name="person_detail_cbv"),
    path('person_create/', PersonCreate.as_view(), name="person_create_cbv"),
    path('person_update/<int:pk>/', PersonUpdate.as_view(), name="person_update_cbv"),
    path('person_delete/<int:pk>/', PersonDelete.as_view(), name="person_delete_cbv"),
    path('person_bulk/', ProdutoBulk.as_view(), name="person_bulk"),
    path('api/', api, name="api"),
    path('apicbv/', APICBV.as_view(), name="apicbv"),
]