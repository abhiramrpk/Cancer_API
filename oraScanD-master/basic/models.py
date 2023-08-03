from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# lets us explicitly set upload path and filename
def scan_upload_to(instance, filename):
    return 'images/scaned_images/{filename}'.format(filename=filename)

def profile_upload_to(instance, filename):
    return 'images/profile/{filename}'.format(filename=filename)



class Print(models.Model):
    image_url = models.ImageField(upload_to=scan_upload_to,null=True)


class MyModel(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    blood_group = models.CharField(max_length=80, blank=False, null=False)
    image_url = models.ImageField(upload_to=profile_upload_to, blank=True, null=True)