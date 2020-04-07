from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

class Warframes(models.Model):
    warframe = models.CharField(max_length=150)
    sexo = models.CharField(max_length=50, null = True)
    clase = models.CharField(max_length=50, null = True)
    descripcion = models.CharField(max_length=255, null = True)

    class Meta:
        db_table = 'warframe'

#class Juegos(models.Model):
#    
#    juego = models.ForeignKey(User, related_name='user_name', on_delete=models.CASCADE, blank=True, null=True)
#    precio = models.ForeignKey(Producto, related_name='producto_name', on_delete=models.CASCADE, blank=True, null=True)
#    genero = models.CharField(max_length=150)
#    precio = models.IntegerField(null = True)
#    cantidad = models.IntegerField(null = True)

#    class Meta:
#        db_table = 'detalles'