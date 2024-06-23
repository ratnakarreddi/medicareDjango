from rest_framework import serializers
from .models import EmployeeMaster
from .models import DepartmentMaster

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMaster
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentMaster
        fields = '__all__'