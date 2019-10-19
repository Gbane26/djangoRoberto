from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=255)

    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Article(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField( upload_to= 'media')
    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    Category_id= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Article_Category")

    def __str__(self):
        return self.title

class Tag(models.Model):
    Category_id= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Tag_Category")

class Instagram(models.Model):
    image=models.ImageField( upload_to= 'media')

    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)

class Newsletter(models.Model):
    email = models.EmailField()
    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Comment(models.Model):
    author = models.CharField(max_length=50) 
    email = models.EmailField(max_length=25)
    message = models.TextField()
    website = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    Article_id= models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment_Article")
    
    def __str__(self):
        return self.author
    