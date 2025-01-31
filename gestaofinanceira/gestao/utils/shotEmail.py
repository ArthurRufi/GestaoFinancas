from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class EmailService:
    """ Classe para envio de e-mails no Django usando Mailtrap """

    def __init__(self, remetente="noreply@seuprojeto.com"):
        self.remetente = remetente

    def enviar_email_simples(self, destinatarios, assunto, mensagem):
        """ Envia um e-mail de texto simples """
        send_mail(
            assunto,
            mensagem,
            self.remetente,
            destinatarios,
            fail_silently=False
        )

    def enviar_email_html(self, destinatarios, assunto, template, contexto):
        """ Envia um e-mail com template HTML """
        html_mensagem = render_to_string(template, contexto)
        mensagem_txt = strip_tags(html_mensagem)  # Remove HTML para fallback

        send_mail(
            assunto,
            mensagem_txt,
            self.remetente,
            destinatarios,
            html_message=html_mensagem,
            fail_silently=False
        )

emailUser = ''
assunto = ''
mensagem = ''
EmailService.enviar_email_simples()