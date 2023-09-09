from django.db import models
from django.contrib.auth.models import User ,Group
from django.db.models.signals import post_save
class Profile(models.Model):

    user= models.OneToOneField(User ,on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True , blank=True , upload_to="image/")

def create_profile(sender , instance , created , **kwargs ):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
      

post_save.connect(create_profile , sender= User)



    