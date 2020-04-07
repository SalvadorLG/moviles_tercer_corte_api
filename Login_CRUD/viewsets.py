from rest_framework import viewsets
from Login_CRUD.models import Warframes
from rest_framework.permissions import IsAuthenticated
from Login_CRUD.serializer import WarframesSerializer

class WarfrmesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Warframes.objects.all()
    serializer_class = WarframesSerializer

#class DetallesViewSet(viewsets.ModelViewSet):
#    permission_classes = [IsAuthenticated]
#    queryset = Detalles.objects.all()
#    serializer_class = DetallesSerializer