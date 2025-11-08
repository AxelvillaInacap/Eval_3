from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esto le dice a Django: "Todo lo que empiece con 'pymes/'
    # envíalo al archivo 'urls.py' de la aplicación 'Pymes'".
    path('pymes/', include('Pymes.urls')), 
]
