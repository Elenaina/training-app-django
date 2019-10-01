from django.shortcuts import render
from .models import Employee, Position
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EmployeeSerializer, PositionSerializer
# Create your views here.


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('surname')
    serializer_class = EmployeeSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
