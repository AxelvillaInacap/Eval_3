from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Empresa
from .forms import EmpresaForm 

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