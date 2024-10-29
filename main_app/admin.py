from django.contrib import admin

# Register your models here.
from .models import Musician, Music

admin.site.register(Musician)
admin.site.register(Music)