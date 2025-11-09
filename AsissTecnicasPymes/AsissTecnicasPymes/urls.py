# AsissTecnicasPymes/AsissTecnicasPymes/urls.py

from django.contrib import admin
from django.urls import path, include
# ¡NUEVO IMPORT! Importamos las vistas de autenticación de Django
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/login/', permanent=True)),
    path('admin/', admin.site.urls),
    path('pymes/', include('Pymes.urls')), # Nuestras rutas de la app
    
    # --- NUEVAS RUTAS DE AUTENTICACIÓN ---
    
    # URL para la página de Login
    path('login/', auth_views.LoginView.as_view(
        template_name='pymes/login.html'
    ), name='login'),
    
    # URL para la página de Logout
    path('logout/', auth_views.LogoutView.as_view(
        template_name='pymes/logout.html'
    ), name='logout'),
    
    # --- FIN DE NUEVAS RUTAS ---
]
