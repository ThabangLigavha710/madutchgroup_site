from django.forms import ModelForm
from django import forms
from .models import Message

class SendMassageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'message'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'validate autocomplete', 'placeholder': 'First Name', 'required': ''}),
            'last_name': forms.TextInput(attrs={'class': 'validate autocomplete', 'placeholder': 'Last Name', 'required': ''}),
            'phone_number': forms.TextInput(attrs={'class': 'validate autocomplete', 'placeholder': 'Phone Number', 'required': ''}),
            'email': forms.EmailInput(attrs={'class': 'validate autocomplete', 'placeholder': 'Email Address', 'required': ''}),
            'message': forms.Textarea(attrs={'class': 'materialize-textarea', 'placeholder': 'Write a message', 'required': ''})
            }