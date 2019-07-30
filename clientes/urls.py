from django.urls import path, include
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
from .views import csv_download
from .views import clientes_upload
from .views import PersonViewSet
from .views import send_email_to_managers
from .api import router

urlpatterns = [
    path('', include(router.urls)),
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
    path('csv-download/', csv_download, name="csv_download"),
    path('upload/', clientes_upload, name="clientes_upload"),
    path('api-clientes/', PersonViewSet, name='api_clientes'),
    path("email/", send_email_to_managers),
]