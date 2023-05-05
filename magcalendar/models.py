from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Exercises(models.Model):
    title = models.CharField(max_length=255, default='')
    title_polish = models.CharField(max_length=255, default='')
    photo_url = models.CharField(max_length=255, default='default.jpg')
    User = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    video_url = models.CharField(max_length=255, default='default.html')
    note =  models.CharField(max_length=255, default='notatka')

class Calendar_exercises(models.Model):
    id_Exercises = models.ForeignKey('Exercises',on_delete=models.CASCADE, default=1)
    id_User = models.ForeignKey(User,on_delete=models.CASCADE)
    note = models.CharField(max_length=255)
    created_at = models.DateField()
    repeats = models.IntegerField()



