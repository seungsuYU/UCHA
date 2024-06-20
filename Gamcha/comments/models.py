from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='author_post')
    subject = models.CharField(max_length=200)