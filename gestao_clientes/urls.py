from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include(home_urls), name='home'),
    path('admin/', admin.site.urls),
    path('clientes/', include(clientes_urls), name='url_clientes'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
