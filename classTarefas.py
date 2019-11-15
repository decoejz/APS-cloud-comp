import pymongo
import bson
import json

class Tarefas:

    def __init__(self,hostip):
        client = pymongo.MongoClient(hostip,27017)
        self.db = client.aplicacao

        dependencias = {}
        with open("./id.json") as json_file:
            data = json.load(json_file)
            for p in data:
                dependencias[p] = data[p]

        self.idTarefa = dependencias["id"]

    def criaTarefa(self,novaTarefa):#TALKEI
        self.db.tarefas.insert_one({"tarefa": novaTarefa, '_id':self.idTarefa})
        self.add_id()
    
    def listaTarefas(self):
        resposta = self.db.tarefas.find()
        temp = {}
        for i in resposta:
            temp[i['_id']] = i['tarefa']

        return temp

    def mostraTarefa(self,tarefaId):
        resposta = self.db.tarefas.find_one({'_id':tarefaId})
        if resposta != None:
            temp = {str(resposta['_id']): resposta['tarefa']}
            return temp
        return None
        
        
    def apagaTarefa(self, tarefaId):
        self.db.tarefas.delete_one({'_id':tarefaId})
        

    def atualizaTarefa(self,tarefaId, atualTarefa):
        resposta = self.db.tarefas.update_one({'_id':tarefaId},{ "$set": { "tarefa": atualTarefa } })
    

    def add_id(self):
        self.idTarefa+=1
        with open('./id.json','w') as f:
            json.dump({"id": self.idTarefa},f)
