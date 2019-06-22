import no


class Automato:

    # ESPECIFICAÇOES DO AUTOMATO
    simbolos = []
    estados = []
    estado_incial = []
    estados_finais = []
    estado_atual: str
    pilha = []

    modulos = []  # LISTA DE NOS DO AUTOMATO

    def __init__(self, gramatica: str):  # CONSTRUTOR DA CLASSSE RECEBENDO A GRAMATICA DO AUTOMATO (1° LINHA DO ARQUIVO)

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
        self.pilha = gramatica[4].split(', ')   # LISTA DE SIMBOLOS DE PILHA

        self.estado_incial = gramatica[2].split(', ')   # RESOLVENDO PROBLEMA DO ESTADO INCIAL JUNTO COM "D"
        self.estado_incial.remove('D')
        for i in self.estado_incial:
            if i == '':   # MAIS ELEMENTOS INUTEIS '-'
                self.estado_incial.remove(i)

        self.estado_atual = self.estado_incial[0]  # O ESTADO ATUAL SERÁ IGUAL AO ESTADO INICIAL

        print(gramatica)

        for i in self.estados:  # CRIANDO OS NOS DO AUTOMATO DE ACORDO COM OS ESTADOS E ADICIONANDO À LISTA DE MODULOS
            NO = no.No(i)   # PASSANDO O NOME DO NO PARA O CONSTRUOTR DA CLASSE
            self.modulos.append(NO)


    #def setprod(self, rea_de_prod: list): #DEFININDO AS REGRAS DE PRODUÇÃO



    #def processa(self, estado, simbolo):
        #TODO est_atual -> est_destino



