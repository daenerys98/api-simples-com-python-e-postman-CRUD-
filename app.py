from flask import Flask, jsonify, request #Jsonify converte valores em javascript para uma String JSON

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J. K. Rowling'
    },
    {
        'id': 2,
        'titulo': 'A Seleção',
        'autor': 'Kiera Cass'
    },
    {
        'id': 3,
        'titulo': 'As Crônicas de Nárnia',
        'autor': 'C. S. Lewis '
    },
]

#consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consultar(id)
@app.route('/livros/<int:id>', methods=['GET']) # Ou seja, ele pega após a / o número inteiro que eu passar e puxa o id correspondente a ele, caso eu coloque http://localhost:5000/livros/1, chamará o livro:Harry Potter e a Pedra Filosofal  
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id: # Retorna o valor da propriedade
            return jsonify(livro)
#editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json() # Pega as informações do usuario para a api
    for indice, livro in enumerate(livros): # Pega o indice e o livro individual
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == 'id':
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)