from django.db import models
from .dataFields import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid
from .functions import generate_token

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , blank=False , null=False)
    emailAddress = models.EmailField(max_length=100, blank=False, null = False)
    date_created = models.DateField(null=True,blank=False,auto_now_add=True)
    date_updated = models.DateField(null=True,blank=False,auto_now=True)
    last_login = models.DateField(null=True,blank=False,auto_now=True)
    token = models.CharField(max_length=32, unique=True, default=generate_token)

    def fullName(self):
        return str(self.user)

    def __str__(self):
        return self.fullName()
    

#> Signal For Updating The Token Each Time The User Data Updated
def updatedProfileToken(sender,instance,created,**kwargs):
    if not created:
        new_token = generate_token()
        myuserProfile = instance.userprofile
        myuserProfile.token = new_token
        myuserProfile.save()
        print("The Token has been updated Successfully")
post_save.connect(updatedProfileToken,sender=User)   