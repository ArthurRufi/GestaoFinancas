import re

class Verify:
    def __init__(self, email: str):
        self.email = email

    def validar_email(self):
        """Verifica se o e-mail armazenado na instância é válido"""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|com\.br)$'
        
        if re.match(padrao, self.email):  # Usa self.email
            print(self.email)
            return True
        else:
            print('Email inválido')
            return False

# Exemplo de uso:
c = Verify("string@gmail.com")
c.validar_email()  # ✅ Agora funciona corretamente
