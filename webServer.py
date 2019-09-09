from tarefas import Tarefas
from flask import Flask, request, jsonify

tf = Tarefas()
app = Flask(__name__)

@app.route('/Tarefa/', methods=['GET', 'POST'])
def mainTarefas():
    if request.method == 'GET':
        return jsonify(tf.listaTarefas())
    elif request.method == 'POST':
        new_tarefa = request.get_json()
        tf.criaTarefa(new_tarefa["nova tarefa"])
    return ('200')

@app.route('/Tarefa/<int:id_tarefa>', methods=['GET', 'PUT', 'DELETE'])
def umaTarefa(id_tarefa):
    if request.method == 'GET':
        return tf.mostraTarefa(id_tarefa)
    elif request.method == 'PUT':
        updated_tarefa = request.get_json()
        tf.atualizaTarefa(id_tarefa,updated_tarefa['tareafa atualizada'])
    elif request.method == 'DELETE':
        tf.apagaTarefa(id_tarefa)
    return ('200')

@app.route('/healthcheck/')
def checkStatus():
    return ('200')

if __name__ == "__main__":
    app.run(debug=True)