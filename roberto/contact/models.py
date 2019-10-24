from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=25)
    message = models.TextField()
    statut=models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name