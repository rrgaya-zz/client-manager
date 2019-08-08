from rest_framework import routers
from .views import PersonViewSet

router = routers.DefaultRouter()
router.register(r"clientes", PersonViewSet)
