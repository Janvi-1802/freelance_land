from django.db import models

# Create your models here.
class projects_request(models.Model):

    client_id=models.CharField(max_length=100,default=0)
    freelancer_id=models.CharField(max_length=1000)
    project_id=models.CharField(max_length=1000)
    #either request is accepted /rejected/not viewd yet
    status=models.CharField(max_length=1000,default="Not viewd yet")