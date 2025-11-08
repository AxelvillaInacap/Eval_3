from django.contrib import admin
from .models import Empresa, Servicio, Profesional, OrdenServicio

# --- Configuración Avanzada para Empresa ---

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Empresa
    en el panel de administración.
    """
    
    # Muestra estos campos como columnas en la vista de lista
    list_display = ('razon_social', 'rut', 'email', 'comuna')
    
    # Añade filtros en el panel derecho basados en estos campos
    list_filter = ('comuna', 'giro')
    
    # Añade una barra de búsqueda que buscará en estos campos
    search_fields = ('razon_social', 'rut', 'email')

# --- Registros para los otros modelos ---
# (compañeros los modifiquen después)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    """
    Personalización del Admin para el modelo Servicio.
    Cumple con R.T. Django Admin.
    """
    
    # Columnas a mostrar en el listado
    list_display = ('nombre', 'categoria', 'dur_est_horas', 'activo')
    
    # Filtros laterales (solicitados por categoría y activo) [cite: 71]
    list_filter = ('categoria', 'activo')
    
    # Campos de búsqueda
    search_fields = ('nombre', 'descripcion', 'categoria')
    
    # Orden por defecto
    ordering = ('nombre',)

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'especialidad', 'email')
    search_fields = ('nombres', 'apellidos', 'run')

@admin.register(OrdenServicio)
class OrdenServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'estado', 'prioridad', 'fecha_creacion')
    list_filter = ('estado', 'prioridad', 'fecha_creacion')
    search_fields = ('empresa__razon_social',) # Búsqueda en un campo ForeignKey