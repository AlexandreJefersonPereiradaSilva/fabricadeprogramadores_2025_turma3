class Pessoa():
    def __init__(self, nome, idade, telefone, cpf, email):
        self.nome = nome
        self.idade = idade
        self._telefone = telefone
        self.__cpf = cpf
        self.__email = email


