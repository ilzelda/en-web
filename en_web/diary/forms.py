from django import forms

class DiaryForm(forms.Form):
    date = forms.DateField()
    description = forms.CharField(widget=forms.Textarea)
