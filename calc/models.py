from django.db import models

# Create your models here.

class courses(models.Model):

    img=models.ImageField(upload_to ='pics')

    date=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    disc=models.TextField()
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    free=models.BooleanField(default=False)
