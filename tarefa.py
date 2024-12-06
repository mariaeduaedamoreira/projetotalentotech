class Tarefa:
    def __init__(self, id, titulo, descricao):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao

    # Getters
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_descricao(self):
        return self.__descricao

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self):
        return f"Tarefa {self.__id}: {self.__titulo} - {self.__descricao}"
