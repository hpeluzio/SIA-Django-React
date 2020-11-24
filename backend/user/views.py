from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = (IsAdminUser, )

    def get_permissions(self):
        """
        list, create, retrieve, update, partial_update, destroy
        """
        if self.action in ['list', 'create']:
            self.permission_classes = (permissions.AllowAny, )
        elif self.action in ['create']:
            self.permission_classes = (permissions.IsAdminUser, )
        else:
            self.permission_classes = (permissions.IsAdminUser, )
        return super(self.__class__, self).get_permissions()

    def create(self, request):
        if request.data['password'] != request.data['confirm_password']:
            return Response({'confirm_password': 'Password must match.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
