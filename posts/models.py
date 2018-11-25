from django.db import models

# Create your models here.
from blogs.models import Blog
from categories.models import Category


class Post(models.Model):
    post_title = models.CharField(max_length=150)
    post_body = models.TextField()
    date_published = models.DateTimeField('%m/%d/%Y %H:%M')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    image = models.URLField()

    def __str__(self):
        return '{0} ({1})'.format(self.post_title, self.blog)