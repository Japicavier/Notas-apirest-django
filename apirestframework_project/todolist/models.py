from django.db import models

# Create your models here.
class Tarea(models.Model):

    ESATOD_CHOICES = (
        ('1', 'Pendiente'),
        ('2', 'Completada'),
    )
    
    descripcion = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=1,choices=ESATOD_CHOICES)
    