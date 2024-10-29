from django.db import models
from django.urls import reverse

# Create your models here.

MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
)

class Musician(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    
    
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