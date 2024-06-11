# Generated by Django 4.2.13 on 2024-06-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeMaster',
            fields=[
                ('employee_master_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('department_id', models.IntegerField(max_length=50)),
                ('status', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]