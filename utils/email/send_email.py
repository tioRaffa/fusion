from django.core.mail.message import EmailMessage

def send_email(name, email_, subject, message):
    conteudo = f'Nome: {name}\nEmail: {email_}\nAssunto: {subject}\nMensagem: {message}'
    
    mail = EmailMessage(
        subject=subject,
        body=conteudo,
        from_email='contatofusion@gmail.com',
        to=['rafaelmuniz200@gmail.com'],  # Lista correta
        reply_to=[email_]
    )
    mail.send()