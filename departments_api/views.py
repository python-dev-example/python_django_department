from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from departments_api.models import Department, Employee
from departments_api.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentGetAllView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)

        return Response(serializer.data)


class DepartmentGetOneView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(department, many=False)

        return Response(serializer.data)


class DepartmentGetPaginatedView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentSaveView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DepartmentSerializer


class DepartmentUpdateView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Department.objects.filter(pk=pk)


class DepartmentDeleteView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Department.objects.filter(pk=pk)


class EmployeeGetAll(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, department_pk):
        employees = Employee.objects.filter(department__id=department_pk)
        serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data)


class EmployeeGetPaginated(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id: int = self.kwargs['department_pk']
        return Employee.objects.filter(department__id=department_id)


class EmployeeGetOneView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        department = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(department, many=False)

        return Response(serializer.data)


class EmployeeSaveView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = EmployeeSerializer


class EmployeeUpdateView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Employee.objects.filter(pk=pk)


class EmployeeDeleteView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Employee.objects.filter(pk=pk)
