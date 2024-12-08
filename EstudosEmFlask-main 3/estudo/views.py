from estudo import app
from flask import render_template, request, redirect, url_for, jsonify
import datetime



itens = []

@app.route('/anonovo/')
def segundapagina():
    agora = datetime.datetime.now()
    return render_template('segundapagina.html', anonovo = agora.month == 1 and agora.day == 1)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        # Obtém o item enviado pelo formulário
        novo_item = request.form.get('item')
        if novo_item:
            itens.append(novo_item)
    
    # Renderiza o template HTML, passando a lista de itens
    return render_template('index.html', itens=itens)


@app.route('/delete/<int:index>', methods=['POST'])
def delete_item(index):
    if index >= 0 and index < len(itens):
        itens.pop(index)
    return redirect(url_for('homepage'))




@app.route('/calculadora/', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    if request.method == "POST":
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operacao = request.form["operacao"]

            if operacao  == "+":
                resultado = num1 + num2

    return render_template ('calculadora.html', resultado=resultado)


'''

@app.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    dados = request.json
    novo_usuario = Usuario(nome=dados['nome'], email=dados['email'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário criado com sucesso!'})


# Rota para listar todos os usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    lista_usuarios = [{'id': u.id, 'nome': u.nome, 'email': u.email} for u in usuarios]
    return jsonify(lista_usuarios)


@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado!'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário deletado com sucesso!'})

    
'''