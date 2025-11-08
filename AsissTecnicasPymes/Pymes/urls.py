from django.urls import path
from . import views  # Importamos las vistas de la app (views.py)

urlpatterns = [
    # URL para la lista de empresas
    # Cuando alguien visite '.../pymes/', se ejecutará la vista 'lista_empresas'
    path('', views.lista_empresas, name='lista_empresas'),
    
    # URL para crear una nueva empresa
    # (GET y POST) /pymes/empresa/crear/
    path('empresa/crear/', views.crear_empresa, name='crear_empresa'),

    # URL para el detalle de una empresa
    # Cuando alguien visite '.../pymes/empresa/5/', se ejecutará la vista 'detalle_empresa'
    # <int:pk> captura el número (ej. 5) y lo pasa a la vista como la variable 'pk'
    path('empresa/<int:pk>/', views.detalle_empresa, name='detalle_empresa'),

    # (GET, POST) /pymes/empresa/5/actualizar/
    path('empresa/<int:pk>/actualizar/', views.actualizar_empresa, name='actualizar_empresa'),

    # (GET, POST) /pymes/empresa/5/eliminar/
    path('empresa/<int:pk>/eliminar/', views.eliminar_empresa, name='eliminar_empresa'),

    path('servicios/', views.lista_servicios, name='lista_servicios'),
    
    # Read (Detail)
    path('servicio/<int:pk>/', views.detalle_servicio, name='detalle_servicio'),
    
    # Create
    path('servicio/crear/', views.crear_servicio, name='crear_servicio'),
    
    # Update
    path('servicio/<int:pk>/actualizar/', views.actualizar_servicio, name='actualizar_servicio'),
    
    # Delete
    path('servicio/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
]
