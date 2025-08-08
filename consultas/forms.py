from django import forms
from .models import Consulta, Categoria, Respuesta

from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        exclude = ['autor']  # Excluye el campo autor

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresá el título de tu consulta',
            }),
            'cuerpo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Describí tu consulta con el mayor detalle posible...',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
        }




class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = '__all__'
