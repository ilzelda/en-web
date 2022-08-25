from django import forms
from .models import Planet, Comment

class PlanetModelForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

