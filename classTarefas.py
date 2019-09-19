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
        try:
            return(self.tarefas_dic[tarefaId])
        except Exception as e:
            return 1

    def apagaTarefa(self, tarefaId):
        try:
            del self.tarefas_dic[tarefaId]
            return 0
        except Exception as e:
            return 1

    def atualizaTarefa(self,tarefaId, atualTarefa):
        try:
            if tarefaId in self.tarefas_dic:
                self.tarefas_dic[tarefaId] = atualTarefa
                return 0
            else:
                raise Exception()
        except Exception as e:
            return 1
