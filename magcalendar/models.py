from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Exercises(models.Model):
    title = models.CharField(max_length=255)


class Calendar_exercises(models.Model):
    id_Exercises = models.ForeignKey('Exercises',on_delete=models.CASCADE, default=1)
    id_User = models.ForeignKey(User,on_delete=models.CASCADE)
    note = models.CharField(max_length=255)
    created_at = models.DateField()
    repeats = models.IntegerField()