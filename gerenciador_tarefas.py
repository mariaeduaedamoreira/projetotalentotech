from tarefa import Tarefa

class GerenciadorTarefas:
    def __init__(self):
        self.__tarefas = []
        self.__proximo_id = 1

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = Tarefa(self.__proximo_id, titulo, descricao)
        self.__tarefas.append(tarefa)
        self.__proximo_id += 1
        return tarefa

    def listar_tarefas(self):
        return self.__tarefas

    def editar_tarefa(self, id, novo_titulo, nova_descricao):
        for tarefa in self.__tarefas:
            if tarefa.get_id() == id:
                tarefa.set_titulo(novo_titulo)
                tarefa.set_descricao(nova_descricao)
                return tarefa
        return None

    def excluir_tarefa(self, id):
        for tarefa in self.__tarefas:
            if tarefa.get_id() == id:
                self.__tarefas.remove(tarefa)
                return tarefa
        return None
