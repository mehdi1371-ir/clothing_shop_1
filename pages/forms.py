from django import forms
from django.core.mail import send_mail


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        content = self.cleaned_data['content']
        send_mail(name, content, email, ['admin@example.com'])