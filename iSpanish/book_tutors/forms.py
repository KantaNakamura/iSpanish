from django import forms

from .models import BookTutors, ReviewOfTutors, EVALUATION_TYPES


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
        
        
class CreateTutorReviewForm(forms.ModelForm):
    review = forms.CharField(label='Review', widget=forms.TextInput(attrs={
        'class': 'form-control', 
        }))
    evaluation = forms.ChoiceField(label='Evaluation', choices=EVALUATION_TYPES, widget=forms.Select(attrs={
        'class': 'form-control', 
        }))
    
    class Meta:
        model = ReviewOfTutors
        fields = ['review', 'evaluation']