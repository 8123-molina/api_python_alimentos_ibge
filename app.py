
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id": 1,
        'titulo': 'O senhor dos aneis',
        'autor': 'J.K Howling 1'
    },
    {
        "id": 2,
        'titulo': 'O senhor dos aneis o retorno do rei',
        'autor': 'J.K Howling 2'
    },
    {
        "id": 3,
        'titulo': 'O senhor dos aneis as duas torres',
        'autor': 'J.K Howling 3'
    }
]

# Consultar todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_to_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar livro por (id)
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_to_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify( "Livro encontrado:",livros[indice], "Será alterado para :", livros[indice])

# Incluir novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir livro (id)
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000,host='localhost',debug=True)