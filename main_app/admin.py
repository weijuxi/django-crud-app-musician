from django.contrib import admin

# Register your models here.
from .models import Musician, Music, Tool

admin.site.register(Musician)
admin.site.register(Music)
admin.site.register(Tool)