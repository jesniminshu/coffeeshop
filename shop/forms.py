from django import forms
from .models import Contact  # Your model

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email', 'phone', 'subject', 'message']  

       