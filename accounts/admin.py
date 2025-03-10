from django.contrib import admin
from .models import Profile

class ProfileAdmin():
    model = Profile


admin.site.register(Profile, ProfileAdmin)