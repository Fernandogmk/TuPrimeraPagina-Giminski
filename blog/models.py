from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    class Estados(models.TextChoices):
        DRAFT = 'B', 'Borrador'
        PUBLISHED = 'P', 'Publicado'
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, choices=Estados.choices, default=Estados.DRAFT)

    def __str__(self):
        return self.titulo