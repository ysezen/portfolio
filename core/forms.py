from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from .utils import OperationResult


class ContactFormValidate(forms.Form):
    name = forms.CharField(
        max_length=254,
        required=True,
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
    )

    def sends_email(self):
        result = OperationResult()
        if self.is_valid():
            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            subject = "Message Received"
            message = self.cleaned_data['message']
            message_context = f'Message Received.\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}'

            try:
                email = EmailMessage(
                    subject,
                    message_context,
                    to=[settings.DEFAULT_FROM_EMAIL],
                    reply_to=[email],
                )
                email.send()

                return result
            except Exception as e:
                result.set_error(str(e), 500)
                return result
        else:
            result.set_error("Contact form is not valid", 400)
            return result




