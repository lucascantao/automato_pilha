import no


class Automato:

    firt_it = True


    # ESPECIFICAÇOES DO AUTOMATO
    simbolos = []
    estados = []
    estado_incial = []
    estados_finais = []
    estado_atual: str
    simbolos_pilha = []

    PILHA= []

    regras_de_prod = []

    modulos = []  # LISTA DE NOS DO AUTOMATO

    def __init__(self, gramatica: str, reg_de_prod: list):  # CONSTRUTOR DA CLASSSE RECEBENDO A GRAMATICA DO AUTOMATO (1° LINHA DO ARQUIVO)

        self.regras_de_prod = reg_de_prod

        # REFORMATANDO A STRING PARA SEPARAR CADA CONJUNTO
        gramatica = gramatica.replace('(', '')
        gramatica = gramatica.replace(')', '')
        gramatica = gramatica.replace('{', '|')
        gramatica = gramatica.replace('}', '|')
        gramatica = gramatica.split('|')  # RECEBE UMA LISTA DOS CONJUNTOS DA GRAMATICA

        # RETIRANDO ELEMENTOS INUTEIS DA LISTA
        for i in gramatica:
            if i == '' or i == ', ':  # TAIS COMO ISSO AÍ ;)
                gramatica.remove(i)

        self.simbolos = gramatica[0].split(', ')   # DEFINIDO LISTA DE SÍMBOLOS
        self.estados = gramatica[1].split(', ')   # DEFININDO LISTA DE ESTADOS
        self.estados_finais = gramatica[3].split(', ')  # LISTA DE ESTADOS FINAIS
        self.simbolos_pilha = gramatica[4].split(', ')   # LISTA DE SIMBOLOS DE PILHA

        self.estado_incial = gramatica[2].split(', ')   # RESOLVENDO PROBLEMA DO ESTADO INCIAL JUNTO COM "D"
        self.estado_incial.remove('D')
        for i in self.estado_incial:
            if i == '':   # MAIS ELEMENTOS INUTEIS '-'
                self.estado_incial.remove(i)

        self.estado_atual = self.estado_incial[0]  # O ESTADO ATUAL SERÁ IGUAL AO ESTADO INICIAL

        print(gramatica)

        for i in self.estados:  # CRIANDO OS NOS DO AUTOMATO DE ACORDO COM OS ESTADOS E ADICIONANDO À LISTA DE MODULOS
            nos = no.No(i)   # PASSANDO O NOME DO NO PARA O CONSTRUOTR DA CLASSE
            self.modulos.append(nos)

    #def setprod(self, reg_de_prod: list): # DEFININDO AS REGRAS DE PRODUÇÃO

     #   for line in reg_de_prod:
      #      print("\nlendo linha:", line)
       #     prod = line.split(', ')
        #    print("split =", prod)
         #   for i in self.modulos:
#
 #               if i.estado_origem == prod[0]:
  #                  i.setNo(prod[1], prod[2], prod[3], prod[4])

    def process(self, simbolo):
        for line in self.regras_de_prod:
            prod = line.split(', ')

            if self.estado_atual == prod[0] and simbolo == prod[1]:

                self.estado_atual = prod[3] # atualizando estado atual

                if self.firt_it: self.firt_it = False  # na primeira interação não a leitura de pilha
                else: self.PILHA.remove(self.PILHA[-1])

                if prod[4] == '-': pass
                else: self.PILHA.append(prod[4])

    def procPal(self, palavra: str):
        for s in palavra:
            self.process(s)



