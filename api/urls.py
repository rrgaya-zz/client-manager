from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('produtos/v1', views.ProdutoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('upload/', views.DafitiUpload),
]

urlpatterns += router.urls
