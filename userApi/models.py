from django.db import models

# Create your models here.
class EmployeeMaster(models.Model):
    employee_master_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    department_id = models.IntegerField(max_length=50)
    status = models.IntegerField(max_length=10)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.employee_name

class DepartmentMaster(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name