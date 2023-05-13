from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
import re

# check username is valid
def validate_username(username):
    pattern = r'^[a-zA-Z0-9_]+$'
    if not re.match(pattern, username):
        raise forms.ValidationError("Your username is not valid. Please enter another username.")
    

class UserRegistForm(forms.ModelForm):
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput(
        attrs={
            'class': 'input mb-4',
            'placeholder': 'password'
    }))
    confirm_password = forms.CharField(label='Confirma Password', widget=forms.PasswordInput(
        attrs={
            'class': 'input mb-4',
            'placeholder': 'confirm_password'
    }))
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4',
            'placeholder': 'username'
        }
    ))
    email = forms.EmailField(label='e-mail', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4',
            'placeholder': 'e-mail'
        }
    ))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password is not correct.')
    
    def save(self, commit=False):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return user
    
    def clean_username(self):
        username = self.cleaned_data['username']
        validate_username(username)
        return username
    

class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(label='e-mail', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4',
            'placeholder': 'e-mail'
        }
    ))
    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={
            'class': 'input mb-4',
            'placeholder': 'password'
        }
    ))