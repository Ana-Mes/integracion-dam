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
        choices = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        )
        fields = ['title', 'content', 'score']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'score': forms.Select(attrs={'class':'form-control'}, choices=choices)

        }
        labels = {
            'title':'', 'content':'', 'score':'Puntuación'
        }