from django.db import models
from users.models import Users

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    