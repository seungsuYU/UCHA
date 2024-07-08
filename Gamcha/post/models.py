from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='author_post')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()
    # like = models.ManyToManyField(User, related_name='like_post')

class Comments(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='author_comments')
    comments = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    # like = models.ManyToManyField(User, related_name='like_answer')
    
