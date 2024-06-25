from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


class Command(BaseCommand):
    help = 'Send a test registration email'

    def handle(self, *args, **kwargs):
        subject = 'Nova inscrição recebida'
        from_email = settings.DEFAULT_FROM_EMAIL
        to = 'naoresponda@acessebank.com.br'

        context = {
            'nome_corretora': 'Teste Corretora',
            'telefone': '(44) 98862-0946',
            'email': 'teste@corretora.com.br',
            'cnpj': '12.345.678/9012-34',
            'pessoa_contato': 'Teste Contato',
        }

        html_content = render_to_string('emails/registration_email.html', context)
        text_content = render_to_string('emails/registration_email.txt', context)

        email = EmailMultiAlternatives(subject, text_content, from_email, [to])
        email.attach_alternative(html_content, "text/html")
        email.send()

        self.stdout.write(self.style.SUCCESS('Test email sent successfully'))
