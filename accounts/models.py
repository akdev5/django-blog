from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Profile Inoframtion with addtional fields portfolio and profile_pic
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #Additional
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
