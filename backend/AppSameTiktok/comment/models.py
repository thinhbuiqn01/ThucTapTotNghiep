from django.db import models

# Create your models here.

from users.models import Users
from post.models import Post

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.TextField()
    category_comment = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)