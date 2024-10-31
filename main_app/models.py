from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length=50)
    # color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tool-detail', kwargs={'pk': self.id})
    
    
class Musician(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    tool = models.ManyToManyField(Tool)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('musician-detail', kwargs={'musician_id': self.id})
    

class Music(models.Model):
        date = models.DateField()
        music_name = models.CharField(max_length=100)
        
        musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.music_name
        
        class Meta:
            ordering = ['-date']