from django import forms

from blogs.models import Blog


class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_title', 'blog_description']