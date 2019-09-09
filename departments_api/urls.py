from django.urls import path

from departments_api import views

urlpatterns = [

    # Departments API
    path(r'get', views.DepartmentGetPaginatedView.as_view()),
    path(r'get/all', views.DepartmentGetAllView.as_view()),
    path(r'<int:pk>/get/', views.DepartmentGetOneView.as_view()),

    path(r'save', views.DepartmentSaveView.as_view()),
    path(r'<int:pk>/update', views.DepartmentUpdateView.as_view()),
    path(r'<int:pk>/delete', views.DepartmentDeleteView.as_view()),

    # Employees API
    path(r'<int:department_pk>/employees/get', views.EmployeeGetPaginated.as_view()),
    path(r'<int:department_pk>/employees/get/all', views.EmployeeGetAll.as_view()),
    path(r'employees/<int:pk>/get', views.EmployeeGetOneView.as_view()),

    path(r'employees/save', views.EmployeeSaveView.as_view()),
    path(r'employees/<int:pk>/update', views.EmployeeUpdateView.as_view()),
    path(r'employees/<int:pk>/delete', views.EmployeeDeleteView.as_view()),
]
