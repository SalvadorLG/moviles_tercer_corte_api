from django.urls import path, include
from Login_CRUD.views import CustomAuthToken, UserConfig
from Login_CRUD.viewsets import WarfrmesViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('warframes',WarfrmesViewSet)

urlpatterns = [
    path('create/', UserConfig.as_view(), name='create'),
    path('login/', CustomAuthToken.as_view(), name='login')
]

urlpatterns += router.urls