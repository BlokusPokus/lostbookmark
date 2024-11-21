from django.db import models

# Create your models here.


class Bookmark(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
