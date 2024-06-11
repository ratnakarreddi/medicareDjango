from django.urls import path
from . import views

# urlPatterns = [
#     path('', views.userApioverview,name='userApioverview'),
# ]
urlpatterns = [
     # path('userApi/', views.userApioverview,name='userApioverview'),
    path('list/', views.employeeList,name='employee-list'),
    path('departmentlist/', views.DepartmentList,name='department-list'),
    path('create/', views.employeeCreate,name='employee-create'),
    path('update/<int:pk>/', views.employeeUpdate,name='employee-update'),
    path('delete/<int:pk>/', views.employeeDelete,name='employee-delete'),
    path('detail/<int:pk>/', views.employeeDetail,name='employee-detail'),
    path('login/', views.employeeData,name='employee-data'),
    
]
