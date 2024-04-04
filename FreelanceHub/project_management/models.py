from django.db import models

from app1.models import *

# Create your models here.
class project_post(models.Model):
    client_id=models.ForeignKey(client,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    Project_discription=models.CharField(max_length=10000)
    # discription_image=models.ImageField(upload_to="media/",default=None)
    # discription_video=models.FileField(upload_to="video/%y",default=None)
    amount=models.CharField(max_length=50)
    




# class project_assign(models.Model):
#     client_id=models.OneToOneField(client,on_delete=models.CASCADE)
#     project_id=models.OneToOneField(project_post,on_delete=models.CASCADE)
#     freelancer_id=models.ManyToOneRel(feild=freelancer_id,on_delete=models.CASCADE)
#     payment_