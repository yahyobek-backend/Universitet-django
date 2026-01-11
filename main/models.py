from django.db import models

# Create your models here.

class Direction(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    is_main = models.BooleanField(default=False)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=(('Erkak', 'Erkak'), ('Ayol', 'Ayol')),max_length=200)
    level = models.CharField(choices=(('Bakalavr','Bakalavr'),('Magistr','Magistr')),max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name