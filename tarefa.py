 #!/usr/bin/env python3
import socket
import sys
import requests

def get_host_address():
    return (socket.gethostbyname(socket.gethostname()))

def add_task(to_add):
    to_add = ' '.join(to_add)

    headers = {
        'content-type': 'application/json'
    }
    data = {
        "nova tarefa": to_add
    }
    res = requests.post('http://'+ip_address+'/Tarefa/', headers=headers, json=data)
    
def list_all():
    res = requests.get('http://'+ip_address+'/Tarefa/')
    print(res.text)

def search_one(task_id):
    res = requests.get('http://'+ip_address+'/Tarefa/'+task_id)
    print(res.text)

def erase_one(task_id):
    res = requests.delete('http://'+ip_address+'/Tarefa/'+task_id)

def update_one(atributos):
    task_id = atributos[0]
    to_update = ' '.join(atributos[1:])

    headers = {
        'content-type': 'application/json'
    }
    data = {
        "tarefa atualizada": to_update
    }
    res = requests.put('http://'+ip_address+'/Tarefa/'+task_id, headers=headers, json=data)

ip_address = get_host_address()
ip_address = "127.0.0.1:5000"

argument = sys.argv[1]
returned = ""

if (argument == "adicionar"):
    add_task(sys.argv[2:])

elif (argument == "listar"):
    list_all()

elif (argument == "buscar"):
    search_one(sys.argv[2])

elif (argument == "apagar"):
    erase_one(sys.argv[2])

elif (argument == "atualizar"):
    update_one(sys.argv[2:])

else:
    print("Argumento inválido!")