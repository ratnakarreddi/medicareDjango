from django.shortcuts import render
from django.views.decorators.http import  require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmployeeMaster
from .serializers import EmployeeSerializer
from .serializers import DepartmentSerializer
from .models import DepartmentMaster
from .models import EmployeeMaster
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['GET'])
def employeeList(request):
    employees = EmployeeMaster.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def DepartmentList(request):
    department = DepartmentMaster.objects.all()
    serializer = DepartmentSerializer(department, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def employeeCreate(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        if 'password' in request.data:
            password = make_password(request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Update'])
def employeeUpdate(request, pk):
    employee = EmployeeMaster.objects.get(employee_master_id=pk)
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['Delete'])
def employeeDelete(requeupdatest, pk):
    employee = EmployeeMaster.objects.get(employee_master_id=pk)
    employee.delete()
    return Response('Employee Deleted')

@api_view(['GET'])
def employeeDetail(request, pk):
    employee = EmployeeMaster.objects.get(employee_master_id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def employeeData(request):
    email = request.data['email_id']
    password = request.data['password']
    employee = EmployeeMaster.objects.get(email_id=email, password=password)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

# Create your views here.

@api_view(['POST'])
def employeeData(request):
    try:
        email = request.data.get('email_id')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            employee = EmployeeMaster.objects.get(email_id=email)
            print(employee);
        except EmployeeMaster.DoesNotExist:
            return Response({'error': 'Invalid email.'}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(password, employee.password):
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
