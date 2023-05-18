from django import forms

from .models import BookTutors


class BookTutorsForm(forms.ModelForm):
    price = forms.CharField(label='Price(dollar)', widget=forms.TextInput(attrs={
        'class': 'form-control', 
        }))
    date = forms.DateField(label='Date', widget=forms.SelectDateWidget(attrs={
        'class': 'form-control', 
        }))
    hour = forms.IntegerField(label='Hour', widget=forms.NumberInput(attrs={
        'class': 'form-control', 
        }))
    
    class Meta:
        model = BookTutors
        fields = ['price', 'date', 'hour']