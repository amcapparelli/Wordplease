from django.db import models

# Create your models here.
from blogs.models import Blog


class Post(models.Model):
    post_title = models.CharField(max_length=150)
    post_body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} ({1})'.format(self.post_title, self.blog)