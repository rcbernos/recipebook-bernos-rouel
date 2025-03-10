from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.OneToOneField(User, max_length=50, on_delete=models.CASCADE)
    short_bio = models.TextField(validators=[MinLengthValidator(50, 'the field must contain at least 50 characters')])
