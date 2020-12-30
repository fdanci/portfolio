from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Your name')
    email = forms.EmailField(required=True, label='Your email')
    subject = forms.CharField(max_length=100, required=True, label='Message subject')
    message = forms.CharField(widget=forms.Textarea, required=True)