from django import forms
from .models import Empresa, Servicio,  Profesional

class EmpresaForm(forms.ModelForm):
    """
    Formulario de Django basado en el modelo Empresa.
    ModelForm se encarga automáticamente de la validación
    basada en los campos definidos en el modelo.
    """
    class Meta:
        # Le dice a ModelForm en qué modelo debe basarse
        model = Empresa

        # Define qué campos del modelo se deben incluir en el formulario
        fields = [
            'rut', 
            'razon_social', 
            'giro', 
            'telefono', 
            'email', 
            'direccion', 
            'comuna'
        ]

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
            'nombre', 
            'apellido', 
            'especialidad', 
            'telefono',    
            'email'
        ]
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }