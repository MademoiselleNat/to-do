from django import forms
from django.contrib.auth.forms import AuthenticationForm

class customForm(AuthenticationForm):
    username = forms.CharField(
        label = '',
        widget = forms.TextInput(
            attrs = {
                'class':'userdata', 
                'placeholder':'Username',
            }
        )
    )
    password = forms.CharField(
        label = '',
        widget = forms.PasswordInput(
            attrs = {
                'class':'userdata',
                'placeholder':'Password',
            }
        )
    )