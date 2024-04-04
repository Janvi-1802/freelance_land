from django.db import models
from django.contrib.auth.models import User 



# Create your models here.




class freelancer(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    freelancer_name=models.CharField(max_length=100)
    user_name=models.TextField()
    password=models.TextField(default=0000)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    phone=models.TextField()
    birthplace=models.TextField()
    profile_pic=models.ImageField(upload_to="profilepic")
    freelancer_contarct=models.FileField(default=None)

class client(models.Model):
    #c=user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    #company name=client_name
    client_name=models.CharField(max_length=100)
    user_name=models.TextField()
    password=models.TextField(default=0000)
    CEO=models.CharField(max_length=100)
    address=models.TextField()
    pincode=models.IntegerField()
    phone=models.TextField()
    email=models.EmailField()
    headquarter=models.CharField(max_length=100)
    website_link=models.URLField(default=None)
    rating=models.IntegerField(default=0)
    comany_certificate=models.FileField(default=None)
    company_contarct=models.FileField(default=None)
