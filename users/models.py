from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    # other user fields and methods...

class Meta:
    permissions = [
        ("can_do_something", "Can do something"),
        # Add other custom permissions here
    ]
