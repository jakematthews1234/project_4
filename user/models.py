from django.db import models
from django.contrib.auth.models import User as AuthorisedUser


class User(AuthorisedUser):
    class Meta:
        proxy = True


