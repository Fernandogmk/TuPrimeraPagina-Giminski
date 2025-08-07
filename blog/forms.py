from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresá el título de tu obra',
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Escribí una descripción o lo que quieras compartir...',
            }),
        }
