from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
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
    }))
    confirm_password = forms.CharField(label='Confirma Password', widget=forms.PasswordInput(
        attrs={
            'class': 'input mb-4',
    }))
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4',
        }
    ))
    email = forms.EmailField(label='e-mail', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4',
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
    


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
            'class': 'input mb-4',
        }))
    confirm_password = forms.CharField(label='Confirma Password', widget=forms.PasswordInput(attrs={
            'class': 'input mb-4',
        }))
    
    class Meta:
        model = get_user_model()
        fields = ['password',]
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwor is not same.')
        
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user