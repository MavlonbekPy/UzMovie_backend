from rest_framework.serializers import ModelSerializer
from .models import MyUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id',  'email')


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id',  'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
