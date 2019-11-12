from classTarefas import Tarefas
from flask import Flask, request, jsonify

tf = Tarefas()
app = Flask(__name__)

@app.route('/Tarefa/', methods=['GET', 'POST'])
def mainTarefas():
    if request.method == 'GET':
        return jsonify(tf.listaTarefas()),200
    elif request.method == 'POST':
        new_tarefa = request.get_json()
        tf.criaTarefa(new_tarefa["nova tarefa"])
        return ('',201)

@app.route('/Tarefa/<int:id_tarefa>', methods=['GET', 'PUT', 'DELETE'])
def umaTarefa(id_tarefa):
    if request.method == 'GET':
        try:
            tarefa_des = tf.mostraTarefa(id_tarefa)
            if (tarefa_des == 1):
                raise Exception('Index not available')
            return str(tarefa_des),200
        except Exception as e:
            return str(e),400
    
    elif request.method == 'PUT':
        try:
            updated_tarefa = request.get_json()
            status = tf.atualizaTarefa(id_tarefa,updated_tarefa['tarefa atualizada'])
            if (status):
                raise Exception('Index not available')
            return('',200)
        except Exception as e:
            return str(e),400
    
    elif request.method == 'DELETE':
        try:
            status = tf.apagaTarefa(id_tarefa)
            if (status):
                raise Exception('Index not available')
            return ('',200)
        except Exception as e:
            return str(e),400

@app.route('/healthcheck/')
def checkStatus():
    return ('Servidor Saudável',200)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8080')
