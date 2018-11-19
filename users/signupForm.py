from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('sorry, someone already use {0} as username. Please pick other username.'.format(username))

    def clean(self):
        data_checked = super().clean()
        if data_checked.get('password') != data_checked.get('repeat_password'):
            raise forms.ValidationError('sorry, \'password\' and \'repeat password\' don`t match')