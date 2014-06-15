from django import forms

from .models import ContactForm

class ContactView(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = ContactForm
