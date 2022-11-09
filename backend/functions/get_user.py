from config import *
from model.user import *

def get_user(email: str):
    return User.query.get(email)

