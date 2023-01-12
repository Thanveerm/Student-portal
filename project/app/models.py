from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User
class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address1 = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
