from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'id': "name",
                'name': "name",
                'placeholder': "Nome",
                'data-error': "Please enter your name"
            }
        )
    )
    
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                'id': "email",
                'name': "email",
                'placeholder': "Email",
                'data-error': "Please enter your email"
            }
        ),
        label=''
    )
    
    subject = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Assunto",
                'id': "msg_subject",
                'class': "form-control", 
                'data-error': "Please enter your subject",
            }
        ),
        label=''
    )
    
    message = forms.CharField(
        max_length=300,
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'id': "message",
                'placeholder': "Mensagem", 
                'rows': "7", 
                'data-error': "Write your message",
            }
        ),
        label=''
    )
    
    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"]
        
        conteudo = f'Nome: {name}\nEmail: {email}\nAssunto: {subject}\nMensagem: {message}'

        from_email = settings.DEFAULT_FROM_EMAIL
    
        try:
            mail = EmailMessage(
                subject=subject,
                body=conteudo,
                from_email='contatofusion@gmail.com',
                to=['rafaelmuniz200@gmail.com'],  
                reply_to=[email]
            )
            mail.send(fail_silently=False)
        except Exception as e:
            print(f'Erro ao enviar o E-mail, {e}')
            raise ValidationError(
                'Erro'
            )
            