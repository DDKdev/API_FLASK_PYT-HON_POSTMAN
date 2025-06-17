from flask import Flask, request, jsonify

app = Flask(__name__)
dados = []

@app.route('/itens', methods=['GET'])
def listar_itens():
    return jsonify(dados)

@app.route('/itens', methods=['POST'])
def adicionar_item():
    item = request.json
    dados.append(item)
    return jsonify({'mensagem': 'Item adicionado'}), 201

@app.route('/itens/<int:indice>', methods=['DELETE'])
def deletar_item(indice):
    if 0 <= indice < len(dados):
        removido = dados.pop(indice)
        return jsonify({'mensagem': 'Item removido', 'item': removido})
    return jsonify({'erro': 'Índice inválido'}), 400

# buscar somente um item da lista
@app.route('/itens/<int:indice>', methods=['GET'])
def obter_item(indice):
    if 0 <= indice < len(dados):
        return jsonify(dados[indice])
    return jsonify({'erro': 'Índice inválido'}), 404

if __name__ == '__main__':
    app.run(debug=True)