from django.db import models
from post.models import Post

# Create your models here.

class Media(models.Model):
    post = models.ForeignKey(Post,related_name="medias", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    media = models.FileField(upload_to='mediaPost/')
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)