from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Tweet Model to store tweets in database

class Tweet(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        con=self.content
        return f"{self.author} => {con[:3]}" 
    

