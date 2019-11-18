import json
from classTarefas import Tarefas
from flask import Flask, request, jsonify

dependencias = {}
with open("/APS-cloud-comp/hosts.json") as json_file:
    data = json.load(json_file)
    for p in data:
        dependencias[p] = data[p]

db_host_ip = dependencias["db_host"]
hostname = dependencias["hostname"]
port = dependencias["port"]

tf = Tarefas(db_host_ip)
app = Flask(__name__)

@app.route('/Tarefa/', methods=['GET', 'POST'])
def mainTarefas():
    if request.method == 'GET':
        return tf.listaTarefas(),200
    elif request.method == 'POST':
        new_tarefa = request.get_json()
        tf.criaTarefa(new_tarefa["nova tarefa"])
        return ('CREATED',201)

@app.route('/Tarefa/<int:id_tarefa>', methods=['GET', 'PUT', 'DELETE'])
def umaTarefa(id_tarefa):
    if request.method == 'GET':
        tarefa_des = tf.mostraTarefa(id_tarefa)
        if (tarefa_des == None):
            return ('NONEXISTENT'),200
        return tarefa_des,200
        
    elif request.method == 'PUT':
        updated_tarefa = request.get_json()
        tf.atualizaTarefa(id_tarefa,updated_tarefa['tarefa atualizada'])
        return 'UPDATED',200
    
    elif request.method == 'DELETE':
        tf.apagaTarefa(id_tarefa)
        return ('DELETED',200)

@app.route('/healthcheck/')
def checkStatus():
    return ('Servidor Saudável',200)

if __name__ == "__main__":
    app.run(debug=True,host=hostname,port=port)
