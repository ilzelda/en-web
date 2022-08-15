from django import forms
from .models import Planet

class PlanetModelForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = ['title']