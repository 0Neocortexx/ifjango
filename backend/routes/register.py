from config import *
from model.user import *
from functions.verify_injection import *
from functions.cripto_pass import *
from functions.verify_pass import *
from functions.get_user import *

@app.route('/register', methods=['GET','POST'])
def registration():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            resposta = jsonify({'resultado':'ok', 'detalhes':'ok'})
            data = request.get_json(force=True)
            user = User(email = data['email'], name = data['name'], password = data['password'])

            for f in filtro:
                if f in user.email or f in user.name or f in user.password:
                    user.email = user.email.replace(f,'')
                    user.email = user.name.replace(f,'')
                    user.password = user.password.replace(f,'')

            if user.email == '' or user.name == '' or user.password == '':
                resposta = jsonify({'resultado': 'nulo'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta

            if '@' not in user.email and len(user.email) <= 6:
                resposta = jsonify({'resultado':'invalido'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta

            a = db.session.query(User.email).filter_by(email = user.email).first()

            if a is not None:
                resposta = jsonify({'resultado':'ja_cadastrado'})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
                return resposta

            user.password = cripto_pass(user.password)
            db.session.add(user) # Adiciona o usuário na tabela.
            db.session.commit()
            resposta = jsonify({'resultado': 'sucesso', 'detalhes': 'ok'})

        except Exception as e:
            # Retorna um erro de cadastro caso ocorra.
            resposta = jsonify({'resultado': 'erro', 'detalhes': str(e)}) 
        resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        try:
            data = request.get_json(force = True)
            email = str(data['email'])
            password = str(data['password'])
            for f in filtro:
                if f in email or f in password:
                    email = email.replace(f,'')
                    password = password.replace(f,'')
            password = password.encode('utf-8') # Deixa a senha no padrão utf-8.
            login = verify_pass(password,email) # Função que verifica a existencia do usuário.
            user = get_user(email) # Select que pega o email e nome do usuário.
            email = user.email
            name = user.name
            jw_token = create_access_token(identity=email)
            resposta = jsonify({'resultado': 'sucesso', 'detalhes': jw_token, 'nome':name,'email':email})
            resposta.headers.add('Access-Control-Allow-Origin', '*')
            if login == False:
                resposta = jsonify({'resultado': 'invalida'})
        except Exception as e:
                resposta = jsonify({'resultado': 'erro', 'detalhes': str(e)})
                resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta
