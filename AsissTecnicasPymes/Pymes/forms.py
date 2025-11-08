from django import forms
from .models import Empresa

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