from estudo import app
from flask import render_template, request

'''
@app.route('/')
def homepage():
    return render_template('index.html')
'''

itens = []

@app.route('/segundapagina/')
def segundapagina():
    return render_template('segundapagina.html')

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        # Obtém o item enviado pelo formulário
        novo_item = request.form.get('item')
        if novo_item:
            itens.append(novo_item)
    
    # Renderiza o template HTML, passando a lista de itens
    return render_template('index.html', itens=itens)
