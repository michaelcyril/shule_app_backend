from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# from school_management.models import *


# Create your models here.

class User(AbstractUser):
    DELETED = 0
    DISABLED = 1
    INACTIVE = 2
    DEFAULT = 3
    ACTIVE = 4
    STATUS_CHOICES = (
        (DELETED, 'User deleted'),
        (DISABLED, 'User disabled'),
        (INACTIVE, 'User inactive'),
        (DEFAULT, 'Default status'),
        (ACTIVE, 'User Active')
    )

    ADMIN = 0
    SCHOOL = 1
    NORMAL = 2
    ROLES_CHOICES = (
        (ADMIN, 'Role admin'),
        (SCHOOL, 'Role school'),
        (NORMAL, 'Norma; user')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=12)

    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    last_password_change = models.DateTimeField(null=True)
    role = models.IntegerField(choices=ROLES_CHOICES, default=NORMAL)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=DEFAULT)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name', 'phone_number', 'username']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'



class Student(models.Model):
    school = models.ForeignKey('school_management.School', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    registration_no = models.CharField(max_length=20)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'Student'


class UserStudent(models.Model):
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'User_student'
