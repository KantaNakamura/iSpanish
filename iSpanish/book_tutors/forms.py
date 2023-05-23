from django import forms

from .models import BookTutors, ReviewOfTutors, EVALUATION_TYPES


class BookTutorsForm(forms.ModelForm):
    price = forms.CharField(label='Price(dollar)', widget=forms.TextInput(attrs={
        'class': 'form-control', 
        }))
    start_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget(attrs={
        'class': 'form-control', 
        }))
    start_time = forms.TimeField(label='Start Time', widget=forms.TimeInput(attrs={
        'class': 'form-control', 
        }))
    end_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget(attrs={
        'class': 'form-control', 
        }))
    end_time = forms.TimeField(label='End Time', widget=forms.TimeInput(attrs={
        'class': 'form-control', 
        }))
    
    class Meta:
        model = BookTutors
        fields = ['price', 'start_date','start_time', 'end_date', 'end_time']
        
        
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