from django import forms

class MyForm(forms.Form):
    email = forms.EmailField(required=True)
