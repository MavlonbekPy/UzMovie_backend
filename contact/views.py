from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from drf_spectacular.utils import extend_schema


class ContactViewSet(ViewSet):
    @extend_schema(responses=ContactSerializer)
    @action(detail=False, methods=['post'])
    def contact(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
