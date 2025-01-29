import re



class Verify():
    def __init__(self, email: str):
        self.email = email

    
    def validar_email(self):
        email = self.email
        # Regex para verificar e-mail com domínio ".com" ou ".com.br"
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|com\.br)$'
        
        if re.match(padrao, email):
            print(email)
            return True
        else:
            print('erro buceta')
            return False


c = Verify("string@gmail.coooom")
c.validar_email()



