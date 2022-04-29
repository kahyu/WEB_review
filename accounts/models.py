from django.db import models
from django.contrib.auth.models import AbstractUser

class userModel(AbstractUser):
    pass

class adminModel(AbstractUser):
    pass
