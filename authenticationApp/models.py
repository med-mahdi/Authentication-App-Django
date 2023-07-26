from django.db import models
from .dataFields import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , blank=False , null=False)
    emailAddress = models.EmailField(max_length=100, blank=False, null = False)
    date_created = models.DateField(null=True,blank=False,auto_now_add=True)
    date_updated = models.DateField(null=True,blank=False,auto_now=True)
    last_login = models.DateField(null=True,blank=False,auto_now=True)

    def fullName(self):
        return str(self.user)

    def __str__(self):
        return self.fullName()