from config import *
from model.user import *
import bcrypt

def verify_pass(senha_dig:str,email_dig:str):
    for q in db.session.query(User.password).filter(User.email==email_dig).all():
        try:
            resultado = bcrypt.checkpw(senha_dig,q[0])
        except:
            return False
        if q == None:
            return False
        return resultado
