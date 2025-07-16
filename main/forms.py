# main/forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'border rounded w-full py-2 px-3',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'border rounded w-full py-2 px-3',
        'placeholder': "Your Email"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'border rounded w-full py-2 px-3',
        'placeholder': 'Your Message'
    }))