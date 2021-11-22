from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(("default.png"), upload_to="media/", height_field=None, width_field=None, max_length=None)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    mle = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    priority = models.CharField(choices=[("High","High"),("medium","medium"),("Low","Low")] ,max_length=20)
    leader = models.ForeignKey(Profile, on_delete=models.RESTRICT ,related_name="leader")
    team = models.ManyToManyField(Profile,related_name="team")
    discription = models.TextField(max_length=1000)

class ListTaskBoard(models.Model):
    project = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    color=models.CharField(max_length=255 ,choices=[('green','green'),('blue','blue')])



class Task(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.OneToOneField(ListTaskBoard,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    progressbar = models.CharField(max_length=255 ) # khassni les  choid de progrestion %
    value = models.CharField( max_length=50)
    date = models.DateField(auto_now=True)
    discreption = models.TextField(max_length=1000)
    

    
    
    
    
    
    