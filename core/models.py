from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    is_active = models.BooleanField()
    city = models.CharField(max_length=50)
