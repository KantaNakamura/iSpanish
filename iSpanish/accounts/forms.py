from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class UserRegistForm(forms.ModelForm):
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput(attrs={
        'class': 'input mb-4'
    }))
    confirm_password = forms.CharField(label='Confirma Password', widget=forms.PasswordInput(attrs={
        'class': 'input mb-4'
    }))
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4'
        }
    ))
    email = forms.EmailField(label='e-mail', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4'
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