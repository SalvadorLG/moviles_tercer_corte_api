from rest_framework import serializers
from .models import User, Producto

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False)
    #is_superuser = serializers.BooleanField(required=False)

    def create(self, validate_data):
        instance = User()
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        #instance.is_superuser = validate_data.get('is_superuser')
        instance.save()

        return instance

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'