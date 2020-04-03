from rest_framework import viewsets
from Login_CRUD.models import Producto
from rest_framework.permissions import IsAuthenticated
from Login_CRUD.serializer import ProductosSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

#class DetallesViewSet(viewsets.ModelViewSet):
#    permission_classes = [IsAuthenticated]
#    queryset = Detalles.objects.all()
#    serializer_class = DetallesSerializer