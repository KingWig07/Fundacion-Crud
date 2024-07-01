from django.db import models
from django.contrib.auth.models import User

class MandatoAporte(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_aportador = models.CharField(max_length=100)
    rut_aportador = models.CharField(max_length=12)
    monto = models.IntegerField()
    numero_tarjeta = models.CharField(max_length=16)
    fecha_inicio = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_aportador} - ${self.monto}"
    