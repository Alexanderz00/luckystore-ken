from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=34)
    photo = models.ImageField(upload_to='photos')
    phone = models.CharField(max_length=30)
    sex = models.CharField(max_length=1)
    email = models.CharField(max_length=100)