from classes_ex_4 import Pessoa
class Pessoa():

    def get_email(self):
        return self.__email
    
    def set_email(self, novo_email):
        self.__email = novo_email

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def falar(self):
        return f"{self.nome} esta falando."
    
    def escrever(self):
        return f"{self.nome} esta escrevendo."
    
    def cantar(self):
        return f"{self.nome} esta cantando."
    
    def ligar(self):
        return f"{self.nome} esta ligando {self.telefone} para pedir uma pizza"
