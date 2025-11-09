from django import forms
from .models import Empresa, Servicio,  Profesional, OrdenServicio


class EmpresaForm(forms.ModelForm):
    """
    Formulario ModelForm para Empresa con widgets de Bootstrap.
    """
    class Meta:
        model = Empresa
        fields = [
            'rut', 
            'razon_social', 
            'giro', 
            'telefono', 
            'email', 
            'direccion', 
            'comuna'
        ]
        
        # 'widgets' le dice a Django cómo renderizar cada campo
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'giro': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 912345678'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@empresa.cl'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ServicioForm(forms.ModelForm):
    """
    Formulario basado en el modelo Servicio (según tu models.py).
    """
    class Meta:
        model = Servicio
        # Campos exactos de tu modelo
        fields = [
            'nombre', 
            'descripcion', 
            'categoria', 
            'dur_est_horas', 
            'activo'
        ]
        
        # Widgets para mejorar la apariencia (opcional pero recomendado)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Diagnóstico de Redes'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'maxlength': 200}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'dur_est_horas': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
    def clean_nombre(self):
        # Limpieza simple de espacios
        return self.cleaned_data['nombre'].strip()
    
class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = [
            'run',
            'nombres', 
            'apellidos', 
            'especialidad',    
            'email'
        ]
        
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan Andrés'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Pérez González'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class OrdenServicioForm(forms.ModelForm):
    """
    Formulario ModelForm para OrdenServicio.
    """
    class Meta:
        model = OrdenServicio
        fields = [
            'empresa',
            'estado',
            'prioridad',
            'des_requerimiento',
            'ser_seleccionados',
            'pro_asignado',
        ]
        
        # Esto (widgets) está perfecto, no lo toques
        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
            'des_requerimiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ser_seleccionados': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            
            'pro_asignado': forms.Select(attrs={'class': 'form-select'}),
        }

    
    def __init__(self, *args, **kwargs):
        """
        Sobrescribe el init para hacer campos opcionales,
        respetando lo definido en el models.py.
        """
        # Llama al 'init' original del formulario
        super().__init__(*args, **kwargs)
        
        # Accede al campo 'pro_asignado' y le quita el 'required'
        self.fields['pro_asignado'].required = False
        
        # Haz lo mismo para 'ser_seleccionados'
        self.fields['ser_seleccionados'].required = False
    