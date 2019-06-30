import automato
import os

path = os.getcwd()              # PEGANDO CAMINHO ATUAL
directory = os.listdir(path)    # LISTANDO TODOS OS ARQUIVOS

arq_list = []

arq: str

for fi in directory:            # ADICIONANDO TODOS OS ARQUIVOS .txt PARA arq_list
    if fi.endswith('.txt'):
        arq_list.append(fi)

# O USUÁRIO DEVERÁ DIZER QUAL O ARQUIVO QUE ESTÁ O AUTÔMATO ATRAVÉS DE UM ÍNDICE NUMÉRICO
while True:
    print("\n%s : \n"%path)
    for i in range(len(arq_list)):
        print("\t", i+1, "-", arq_list[i])

    opc = int(input("\nIndique o arquivo a ser lido: "))

    if 0 < opc < len(arq_list)+1:
        arq = arq_list[opc-1]
        print("\n")
        break
    else:
        print("\nÍndice = %d inválido! Por favor, digite novamente." % opc)


file = open(arq, 'r', encoding='utf-8')

a = file.read()
line = a.splitlines()

gramatica = line[0]   # PRIMEIRA LINHA DO ARQUIVO CONTENDO A GRAMATICA DO AUTOMATO
regras_de_prod = line[1:]

aut = automato.Automato(gramatica, regras_de_prod)  # PASSANDO A STRING DA PRIMEIRA LINHA DO ARQUIVO COMO PARÂMETRO

print("SIMBOLOS: ", aut.simbolos)
print('ESTADO INICIAL: ', aut.estado_incial)
print('ESTADOS FINAIS: ', aut.estados_finais)
print('ESTADOS: ', aut.estados)
print('PILHA: ', aut.simbolos_pilha)
print('ESTADO ATUAL: ', aut.estado_atual)

print(regras_de_prod)

palavra = input("Digite a palavra:\n")

aut.processa_palavra(palavra)
