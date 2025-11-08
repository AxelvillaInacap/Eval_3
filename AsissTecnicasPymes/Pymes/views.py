from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Empresa
from .forms import EmpresaForm 
from .models import Servicio
from .forms import ServicioForm
from .models import Profesional
from .forms import ProfesionalForm

def lista_empresas(request):
    """
    Esta vista muestra una lista de todas las empresas.
    Ahora también maneja la búsqueda (filtro) por GET.
    """
    
    # Obtiene el término de búsqueda desde la URL (parámetro GET 'q')
    query = request.GET.get('q')

    # Inicialmente, obtenemos todas las empresas
    empresas = Empresa.objects.all()

    # 3. Si hay un término de búsqueda (query no es None o vacío)
    if query:
        # 4. Filtramos el queryset 'empresas'
        # Usamos Q() para poder buscar en múltiples campos con 'OR'
        # icontains = 'case-insensitive contains' (contiene, sin importar mayúsculas/minúsculas)
        empresas = empresas.filter(
            Q(razon_social__icontains=query) | 
            Q(rut__icontains=query)
        )

    # Preparamos el contexto para enviar los datos a la plantilla
    contexto = {
        'empresas': empresas,
        'query': query, # Le pasamos el 'query' a la plantilla
    }

    return render(request, 'pymes/lista_empresas.html', contexto)

def detalle_empresa(request, pk):
    """
    Esta vista muestra los detalles de una empresa específica.
    """
    empresa = get_object_or_404(Empresa, pk=pk)
    contexto = {'empresa': empresa}
    return render(request, 'pymes/detalle_empresa.html', contexto)


def crear_empresa(request):
    """
    Vista para crear una nueva empresa.
    - Si es GET, muestra el formulario vacío.
    - Si es POST, valida los datos y crea la empresa.
    """
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm()

    contexto = {
        'form': form
    }
    return render(request, 'pymes/empresa_form.html', contexto)


def actualizar_empresa(request, pk):
    """
    Vista para actualizar una empresa existente.
    - Si es GET, muestra el formulario con los datos actuales.
    - Si es POST, valida los datos y actualiza la empresa.
    """
    empresa = get_object_or_404(Empresa, pk=pk)
    
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm(instance=empresa)

    contexto = {
        'form': form
    }
    return render(request, 'pymes/empresa_form.html', contexto)


def eliminar_empresa(request, pk):
    """
    Vista para eliminar una empresa existente.
    - Si es GET, muestra una página de confirmación.
    - Si es POST, elimina la empresa y redirige a la lista.
    """
    empresa = get_object_or_404(Empresa, pk=pk)
    
    if request.method == 'POST':
        empresa.delete()
        return redirect('lista_empresas')
        
    contexto = {
        'empresa': empresa
    }
    return render(request, 'pymes/empresa_confirm_delete.html', contexto)

def lista_servicios(request):
    """
    Lista servicios con búsqueda por nombre o categoría.
    Cumple con R.F. 1.a (listar) y 2 (Búsqueda)[cite: 68, 71].
    """
    query = request.GET.get('q', '').strip()
    
    if query:
        # Búsqueda por nombre O categoría (usando Q objects)
        servicios = Servicio.objects.filter(
            Q(nombre__icontains=query) |
            Q(categoria__icontains=query)
        ).order_by('nombre')
    else:
        servicios = Servicio.objects.all().order_by('nombre')
        
    context = {
        'servicios': servicios,
        'query': query
    }
    return render(request, 'Pymes/lista_servicios.html', context)


def detalle_servicio(request, pk):
    """
    Muestra el detalle de un servicio.
    Cumple con R.F. 1.a (ver detalle)[cite: 68].
    """
    servicio = get_object_or_404(Servicio, pk=pk)
    context = {
        'servicio': servicio
    }
    return render(request, 'Pymes/detalle_servicio.html', context)


# --- CREACIÓN (Create) ---

@login_required  # Requiere autenticación [cite: 84]
def crear_servicio(request):
    """
    Crea un nuevo servicio.
    Cumple con R.F. 1.a (Crear)[cite: 68].
    """
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Servicio creado exitosamente!')
            return redirect('lista_servicios')
        else:
            messages.error(request, 'Error al crear el servicio. Revisa los campos.') 
    else:
        form = ServicioForm()
        
    context = {
        'form': form,
        'titulo': 'Crear Nuevo Servicio'
    }
    return render(request, 'Pymes/servicio_form.html', context)


# --- ACTUALIZACIÓN (Update) ---

@login_required  # Requiere autenticación [cite: 84]
def actualizar_servicio(request, pk):
    """
    Actualiza un servicio existente.
    Cumple con R.F. 1.a (actualizar)[cite: 68].
    """
    servicio = get_object_or_404(Servicio, pk=pk)
    
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Servicio actualizado exitosamente!')
            return redirect('detalle_servicio', pk=servicio.pk)
        else:
            messages.error(request, 'Error al actualizar. Revisa los campos.')
    else:
        form = ServicioForm(instance=servicio)
        
    context = {
        'form': form,
        'titulo': f'Actualizar Servicio: {servicio.nombre}'
    }
    return render(request, 'Pymes/servicio_form.html', context)


@login_required  # Requiere autenticación 
def eliminar_servicio(request, pk):
    """
    Elimina un servicio (con confirmación).
    Cumple con R.F. 1.a (eliminar)[cite: 68].
    """
    servicio = get_object_or_404(Servicio, pk=pk)
    
    if request.method == 'POST':
        nombre_servicio = servicio.nombre
        servicio.delete()
        messages.success(request, f'Servicio "{nombre_servicio}" eliminado.')
        return redirect('lista_servicios')
        
    context = {
        'servicio': servicio
    }
    return render(request, 'Pymes/servicio_confirm_delete.html', context)

# Muestra una lista con los datos de los profesionales
@login_required
def lista_profesionales(request):
    consulta = request.GET.get('q', '').strip()

    if consulta:
        profesionales = Profesional.objects.filter(
            Q(nombre__icontains=consulta) |
            Q(apellido__icontains=consulta) |
            Q(especialidad__icontains=consulta)
        ).order_by('apellido', 'nombre')
    else:
        profesionales = Profesional.objects.all().order_by('apellido', 'nombre')

        context = {
            'profesionales': profesionales,
            'consulta': consulta
        }
        return render(request, 'Pymes/lista_profesionales.html', context)

# Muestra el detalle de un profesional
@login_required
def detalle_profesional(request, pk):

    profesional = get_object_or_404(Profesional, pk=pk)
    context = {
        'profesional': profesional
    }
    return render(request, 'Pymes/detalle_profesional.html', context)

# Permite crear un nuevo profesional
@login_required
def crear_profesional(request):
    
    if request.method == 'POST':
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Profesional creado exitosamente!')
            return redirect('lista_profesionales')
        else:
            messages.error(request, 'Error al crear el profesional. Revisa los campos.')
    else:
        form = ProfesionalForm()
        
    context = {
        'form': form,
        'titulo': 'Crear Nuevo Profesional' # Para reutilizar la plantilla
    }
    return render(request, 'Pymes/profesional_form.html', context)

# Permite Actualizar datos de un profesional existente
@login_required
def actualizar_profesional(request, pk):

    profesional = get_object_or_404(Profesional, pk=pk)
    
    if request.method == 'POST':
        form = ProfesionalForm(request.POST, instance=profesional)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Profesional actualizado exitosamente!')
            return redirect('detalle_profesional', pk=profesional.pk)
        else:
            messages.error(request, 'Error al actualizar. Revisa los campos.')
    else:
        form = ProfesionalForm(instance=profesional)
        
    context = {
        'form': form,
        'titulo': f'Actualizar Profesional: {profesional.nombres} {profesional.apellidos}'
    }
    return render(request, 'Pymes/profesional_form.html', context)

# Permite eliminar un profesional existente
@login_required
def eliminar_profesional(request, pk):

    profesional = get_object_or_404(Profesional, pk=pk)
    
    if request.method == 'POST':
        nombre_profesional = f"{profesional.nombres} {profesional.apellidos}"
        profesional.delete()
        messages.success(request, f'Profesional "{nombre_profesional}" eliminado.')
        return redirect('lista_profesionales')
        
    context = {
        'profesional': profesional
    }
    return render(request, 'Pymes/profesional_confirm_delete.html', context)