from django import forms
from .models import DivingSpot, Comment

class DivingSpotForm(forms.ModelForm):

    class Meta:
        model = DivingSpot
        fields = ['name', 'description', 'image', 'location', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Localización'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'latitude': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Latitud'}),
            'longitude': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Longitud'}),

        }
        labels = {
            'name':'', 'description':'', 'image':'', 'location':'', 'latitude':'Latitud', 'longitude':'Longitud'
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
        fields = ['content', 'score']
        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'score': forms.Select(attrs={'class':'form-control'}, choices=choices)

        }
        labels = {
            'content':'', 'score':'Puntuación'
        }