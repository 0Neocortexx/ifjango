from config import *

filtro = ('alert.','<script>','<','>','javascript',';','--',",","=","+",'/',"'",'"',"src=","admin'--"
            ,"or 1=1", "delete from usuario", "document.write","sessionStorage.","Window.","document.",'href=',"]>")

def verifica_injecao(dado: str):
    for f in filtro: # laço de repetição que verifica se não há um texto suspeito de possuir injeção XSS ou SQL.
        if f in dado:
            resposta = dado.replace(f,'')
    if dado == '':
        resposta = None
    return resposta
