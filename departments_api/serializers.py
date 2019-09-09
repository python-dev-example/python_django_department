from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        max_length=100,
        allow_blank=False,
        allow_null=False,
        validators=[
            UniqueValidator(
                queryset=Department.objects.all(),
                message='Department with this name is already exists'
            )
        ]
    )
    description = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        instance = Department(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    class Meta:
        model = Department
        fields = ('id', 'name', 'description', 'create_date', 'update_date')


class DepartmentShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class EmployeeSerializer(serializers.ModelSerializer):
    # department = DepartmentShortSerializer()

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthday = serializers.DateField()
    # birthday = serializers.Mone()
    username = serializers.CharField(
        max_length=50,
        required=True,
        allow_blank=False,
        validators=[
            UniqueValidator(
                queryset=Employee.objects.all(),
                message='Employee with this username is already exists'
            )
        ]
    )
    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        validators=[
            UniqueValidator(
                queryset=Employee.objects.all(),
                message='Employee with this email is already exists'
            )
        ]
    )

    def create(self, validated_data):
        instance = Employee(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.salary = validated_data.get('salary', instance.salary)

        instance.save()
        return instance

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'birthday', 'salary', 'department')
