from django.db import models

class School(models.Model):
    ALEVEL = 0
    OLEVEL = 1
    TYPE_CHOICES = (
        (ALEVEL, 'A level'),
        (OLEVEL, 'O level'),
    )
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'School'


class Event(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_at = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'Event'


class UserSchool(models.Model):
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'User_school'


class Application(models.Model):
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'Application'


class Document(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    document = models.FileField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'Document'




