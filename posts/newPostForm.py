from django import forms
from django.forms import SelectDateWidget, SplitDateTimeWidget

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'date_published': SelectDateWidget()
        }
        labels = {
            'date_published': 'Publish Date '
        }
        fields = ['post_title', 'post_body', 'categories',  'date_published']

