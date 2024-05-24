from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, RegisterSerializer


class AuthenticationViewSet(ViewSet):
    def SignUp(self, request, *args, **kwargs):
        data = request.data
        data['password'] = data['password']
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'user': serializer.data,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def ResetPassword(self, request, *args, **kwargs):
        pass

    def Me(self, request):
        permission_classes = [IsAuthenticated]
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        user = request.user
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_200_OK
        )
