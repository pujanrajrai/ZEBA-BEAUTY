from django import forms
from .models import Booking, NewsletterSubscriber, Contact
from captcha.fields import CaptchaField


class CaptchaFieldForm(forms.Form):
    captcha = CaptchaField()


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 bg-transparent p-2 rounded', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border border-gray-300 bg-transparent p-2 rounded', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'w-full border border-gray-300 bg-transparent p-2 rounded', 'placeholder': 'Phone'}),
            'date': forms.DateInput(attrs={'class': 'w-full border border-gray-300 bg-transparent p-2 rounded', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'w-full border border-gray-300 bg-transparent p-2 rounded', 'type': 'time'}),
            'reason': forms.Textarea(attrs={'class': 'w-full border border-gray-300 bg-transparent p-2 rounded', 'rows': 3, 'placeholder': 'Enter the reason for booking'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 bg-transparent p-2 rounded', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border border-gray-300 bg-transparent p-2 rounded', 'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'class': 'border border-gray-300 bg-transparent p-2 rounded', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'border border-gray-300 bg-transparent p-2 rounded', 'placeholder': 'Your Message', 'rows': 3}),
            'phone_number': forms.TextInput(attrs={'class': 'border border-gray-300 bg-transparent p-2 rounded', 'placeholder': 'Your Phone Number'}),

        }


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'w-60 border border-white bg-transparent p-2 rounded-full',
                'placeholder': 'Type your email'
            }),
        }
