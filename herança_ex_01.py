from classe_pai import Personagem

class Mono(Personagem):
    def __init__(self, nome, sexo, caracteristica, habilidade, entidade):
        super().__init__(nome, sexo, caracteristica, habilidade, entidade)
        
    def modo_de_uso(self):
        print(f'eu me chamo Mono e tenho {self.habilidade}')

class Six(Personagem):
    def __init__(self, nome, sexo, caracteristica, habilidade, entidade, joias):
        super().__init__(nome, sexo, caracteristica, habilidade, entidade)
        self.joias = joias

    def modo_de_uso(self):
        print(f'eu me chamo Six e tenho uma {self.caracteristica}')

class Runaway_kid(Personagem):
    
    def modo_de_uso(self):
        print(f'eu me chamo Runaway Kid e sou hospedeiro de {self.entidade}')

class Lincey(Personagem):

    def modo_de_uso(self):
        print(f'eu me chamo Lincey e sou muito {self.caracteristica}')

class Low(Personagem):
   
    def modo_de_uso(self):
        print(f'eu me chamo Low e sou hospedeiro do {self.entidade}')
    






        
    






        
