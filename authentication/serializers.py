from rest_framework.serializers import ModelSerializer
from .models import MyUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['username'], validated_data['email'],
                                          validated_data['password'])

        return user
