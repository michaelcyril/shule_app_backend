from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.forms import PasswordChangeForm
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'phone_number',
            'full_name',
            'roles',
            'status'
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class StudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'school',
            'name',
            'registration_no'
        ]


class StudentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'school',
            'name',
            'registration_no'
        ]
        depth = 2


class UserStudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStudent
        fields = [
            'user',
            'student',
        ]


class UserStudentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStudent
        fields = [
            'id',
            'user',
            'student',
        ]
        depth = 2
