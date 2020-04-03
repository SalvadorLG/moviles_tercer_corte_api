from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

class Producto(models.Model):
    producto = models.CharField(max_length=150)
    precio = models.IntegerField(null = True)
    cantidadTotal = models.IntegerField(null = True)
    codigo = models.CharField(max_length=150)

    class Meta:
        db_table = 'producto'

#class Detalles(models.Model):
#    id_usuario = models.ForeignKey(User, related_name='user_name', on_delete=models.CASCADE, blank=True, null=True)
#    id_producto = models.ForeignKey(Producto, related_name='producto_name', on_delete=models.CASCADE, blank=True, null=True)
#    codigo = models.CharField(max_length=150)
#    precio = models.IntegerField(null = True)
#    cantidad = models.IntegerField(null = True)

#    class Meta:
#        db_table = 'detalles'