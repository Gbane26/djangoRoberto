from django.db import models

# Create your models here.

class Room(models.Model):
    titre = models.CharField(max_length=50)
    prix = models.IntegerField()
    image = models.ImageField(upload_to='media/room')
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre