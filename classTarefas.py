class Tarefas:

    def __init__(self):
        self.tarefas_dic = {}
        self.idTarefa = 1

    def criaTarefa(self,novaTarefa):
        self.tarefas_dic[self.idTarefa] = novaTarefa
        self.idTarefa += 1
    
    def listaTarefas(self):
        return(self.tarefas_dic)

    def mostraTarefa(self,tarefaId):
        return(self.tarefas_dic[tarefaId])

    def apagaTarefa(self, tarefaId):
        del self.tarefas_dic[tarefaId]

    def atualizaTarefa(self,tarefaId, atualTarefa):
        self.tarefas_dic[tarefaId] = atualTarefa
