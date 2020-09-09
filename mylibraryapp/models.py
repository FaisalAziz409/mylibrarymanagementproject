from django.db import models

# Create your models here.
class Signup(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    address2=models.CharField(max_length=255)
    city=models.CharField(max_length=155)
    state=models.CharField(max_length=155)
    zip=models.IntegerField()
    is_student =models.BooleanField()
    is_teacher =models.BooleanField(default=False)


    def __str__(self):
        return self.email




