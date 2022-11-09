from config import *
import bcrypt

def cripto_pass(senha: str):
        """Criptografa a senha usando o bcrypt."""
        senha = senha.encode('utf-8') # Deixa a senha no padrão utf-8.
        nova_senha = bcrypt.hashpw(senha,bcrypt.gensalt()) # Gera a senha criptografada
        senha = nova_senha
        return senha
