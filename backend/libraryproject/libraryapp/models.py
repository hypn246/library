from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(User):
    avatar = models.ImageField(upload_to='upload/')


