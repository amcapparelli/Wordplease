from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_description = models.TextField()
    blog_url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.blog_title)