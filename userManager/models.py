from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    blog = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=32, blank=True)
    age = models.IntegerField(max_length=2)

    ##       据说创建Admin这个内部类后，会自动有add, create   和delete三种权限
    class Admin:
        list_display = ('user', 'blog', 'email')


class USCitizen(models.Model):
    #

    class Meta:
        permissions = (
            ("can_drive", "Can drive"),
            ("can_vote", "Can vote in elections"),
            ("can_drink", "Can drink alcohol")
        )