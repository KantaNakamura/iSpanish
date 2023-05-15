from django import forms

from accounts.models import Users


class UpdateProfileForm(forms.ModelForm):
    icon = forms.FileField(label='Icon', widget=forms.FileInput(attrs={
        'class': 'form-control', 
        'type': 'file',
        'id': 'formFile',
        }))
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'type': 'text'
        }))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'type': 'text'
        }))
    sex = forms.CharField(label='Sex', widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'type': 'text'
        }))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={
        'class': 'form-control', 
        }))
    is_tutor = forms.BooleanField(label='Country', required=False, widget=forms.CheckboxInput(attrs={
        'type': 'checkbox',
    }))
    description = forms.CharField(label='description', widget=forms.TextInput(attrs={
        'class': 'form-control', 
        }))
    introductory_video_link = forms.URLField(label='introductory_video_link', widget=forms.URLInput(attrs={
        'class': 'form-control', 
        }))

    
    class Meta:
        model = Users
        fields = ['icon', 'name', 'age', 'sex', 'country', 'is_tutor', 'description', 'introductory_video_link']
        
    def save(self, *args, **kwargs):
        obj = super(UpdateProfileForm, self).save(commit=False)
        obj.save()
        return obj