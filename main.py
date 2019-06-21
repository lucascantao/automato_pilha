from automato import *

simbolos = []
estados = []
pilha = []
estados_finais = []
estado_inicial: ""
estado_atual: ""
regras_de_prod = []


file = open("automato_teste.txt", 'r', encoding='utf-8') #

a = file.read()
line = a.splitlines()

gramatica = line[0]
regras_de_prod = line[1:]

aut = Automato(gramatica)

print("SIMBOLOS: ", aut.simbolos)
print('ESTADO INICIAL: ', aut.estado_incial)
print('ESTADOS FINAIS: ', aut.estados_finais)
print('ESTADOS: ', aut.estados)
print('PILHA: ', aut.pilha)
print('ESTADO ATUAL: ', aut.estado_atual)
