from rest_framework import serializers
from .models import Employee, Position


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'position', 'employed_since','salary', 'image', 'is_present', 'leave_left']


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['position_name', 'position_desc']