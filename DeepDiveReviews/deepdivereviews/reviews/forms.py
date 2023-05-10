from django import forms
from .models import DivingSpot, Comment

class DivingSpotForm(forms.ModelForm):

    class Meta:
        model = DivingSpot
        fields = ['name', 'description', 'image', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Localización'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),

        }
        labels = {
            'name':'', 'description':'', 'image':'', 'location':''
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'', 'content':''
        }