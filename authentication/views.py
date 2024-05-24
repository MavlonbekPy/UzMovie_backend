from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import MyUser
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer, RegisterSerializer


class AuthenticationViewSet(ViewSet):
    def SignUp(self, request, *args, **kwargs):
        data = request.data
        password = make_password(data['password'])
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def SignIn(self, request, *args, **kwargs):
        pass

    def ResetPassword(self, request, *args, **kwargs):
        pass

    def Me(self, request):
        if not request.user.is_authenticated:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={'detail': 'Not authenticated'}
            )
        user = MyUser.objects.get()
        return Response(
            status=status.HTTP_200_OK,
            data=UserSerializer(user).data
        )
