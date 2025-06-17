
# GET
#Flask(__name__): Inicializa a aplicação Flask.
#@app.route(): Define a URL que será acessada para chamar essa função.
#jsonify(): Converte os dados Python para o formato JSON.
#app.run(debug=True): Inicia o servidor local.


from flask import Flask, jsonify, request

app = Flask(__name__)

posts = [
        {"id": 1, "titulo": "Post 1", "conteudo": "Conteudo do post 1"},
        {"id": 2, "titulo": "Post 2", "conteudo": "Conteúdo do post 2"}
    ]

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# POST

# new_post = request.get_json() :Recebe os dados em formato JSON
# Adiciona o novo post à lista: posts.append(new_post)
# Retorna o post criado: return jsonify(new_post), 201  


@app.route('/api/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    posts.append(new_post)
    return jsonify(new_post), 201

# DELETE

#Rota DELETE /api/posts/<int:post_id>:
#O <int:post_id> é um parâmetro de URL que define qual post será excluído com base no ID.
#A função delete_post(post_id):
#Busca o post com o ID fornecido.
#Se o post for encontrado, ele remove da lista de posts.
#Se o post não for encontrado, retorna um erro 404 dizendo "Post não encontrado".
#Caso o post seja excluído com sucesso, retorna uma mensagem confirmando a exclusão.


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):

    post = next((post for post in posts if post['id'] == post_id), None)# Encontra o post pelo ID
    if post is None:
        return jsonify({"error": "Post não encontrado"}), 404 # Se o post não for encontrado, retorna um erro 404
    posts.remove(post)# Remove o post da lista
    return jsonify({"message": f"Post {post_id} excluído com sucesso!"}), 200

# MÉTODO MAIN

#SEMPRE QUE QUISER EXECUTAR UMA FUNÇÃO,
#EXECUTE A CÉLULA COM O MÉTODO DESEJADO E DEPOIS A CÉLULA ABAIXO


if __name__ == '__main__':
    app.run(debug=True)