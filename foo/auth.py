__author__ = 'yangq'
from django.contrib.auth.models import User


def createUser(name, password, email=None):
    user = User.objects.create_user(name, email, password)
    user.save()