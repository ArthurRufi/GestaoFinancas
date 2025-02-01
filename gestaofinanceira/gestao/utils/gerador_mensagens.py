from gestaofinanceira.gestao.utils.shotEmail import EmailService

# Classe para envio de e-mail de recuperação de senha
class EmailPasswordRecover:
    def __init__(self):
        # Instancia o serviço de e-mail
        self.email_service = EmailService()

    def emailDeConfirmacao(self, destinatarios, assunto, contexto):
        """ Envia um e-mail para confirmação de recuperação de senha """
        # Define o caminho para o template de recuperação de senha
        templateSelect = "utils/recovery.html"  # O caminho do template é relativo à pasta templates
        # Envia o e-mail com o template e o contexto
        self.email_service.enviar_email(destinatarios=destinatarios, 
                                        template=templateSelect, 
                                        assunto=assunto, 
                                        contexto=contexto)

# Classe de Notificação de Gastos Excessivos (ainda não implementada)
class EmailExcessiveSpending:
    pass
