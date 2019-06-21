from automato import *
import os

path = os.getcwd()              #PEGANDO CAMINHO ATUAL
directory = os.listdir(path)    #LISTANDO TODOS OS ARQUIVOS

arq = ""

for fi in directory:            #DEFININDO ARQUIVO .TXT A SER LIDO
    if fi.endswith('.txt'):
        arq = fi

simbolos = []
estados = []
pilha = []
estados_finais = []
estado_inicial: ""
estado_atual: ""
regras_de_prod = []


file = open(arq, 'r', encoding='utf-8')

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
