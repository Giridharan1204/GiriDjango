from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.name