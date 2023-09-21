from django import forms

class uploadfileform(forms.Form):
    file = forms.FileField()