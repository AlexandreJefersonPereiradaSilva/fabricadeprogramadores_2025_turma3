from classe_pai import Personagem
from herança_ex_01 import *
personagem01 = Mono("Mono", "M", "esperteza", "teleporte", "Homem Magro" )
personagem02 = Six("Six", "F", "fome insaciavel", "abersoção de força vital", "Gueixa", "Joia Vermelha")
personagem03 = Runaway_kid("Runaway Kid", "M","criatividade", "saber nadar", "Grandpa")
personagem04 = Lincey("Lincey", "F", "agil", "nenhuma", "nenhuma")
personagem05 = Low("Low", "M", "criatividade", "especialista em arco e flecha", "Mestre dos espelhos")

def apresentar(qualquer_personagem):
    print(f"Tentando apresentar com {qualquer_personagem.nome}")
    qualquer_personagem.modo_de_uso()

print("-")
apresentar(personagem01)
print("-")
apresentar(personagem02)
print("-")
apresentar(personagem03)
print("-")
apresentar(personagem04)
print("-")
apresentar(personagem05)

#polimorfismo_ex_01 e polimorfismo_ex_02