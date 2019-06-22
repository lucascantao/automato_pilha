import no


class Automato:

    # ESPECIFICAÇOES DO AUTOMATO
    simbolos = []
    estados = []
    estado_incial = []
    estados_finais = []
    estado_atual: str
    pilha = []

    campos = [] # VARIAVEL TEMPORARIA PRA RECEBER A PRIMEIRA LINHA DO ARQUIVO

    modulos = []  # LISTA DE NOS DO AUTOMATO

    def __init__(self, gramatica: str):  # CONSTRUTOR DA CLASSSE RECEBENDO A GRAMATICA DO AUTOMATO (1° LINHA DO ARQUIVO)

        # REFORMATANDO A STRING PARA SEPARAR CADA CONJUNTO
        gramatica = gramatica.replace('(', '')
        gramatica = gramatica.replace(')', '')
        gramatica = gramatica.replace('{', '|')
        gramatica = gramatica.replace('}', '|')
        self.campos = gramatica.split('|')  # CAMPOS RECEBE UMA LISTA DOS CONJUNTOS DA GRAMATICA

        # RETIRANDO ELEMENTOS INUTEIS DA LISTA
        for i in self.campos:
            if i == '' or i == ', ':  # TAIS COMO ISSO AÍ ;)
                self.campos.remove(i)

        self.simbolos = self.campos[0].split(', ')   # DEFINIDO LISTA DE SÍMBOLOS
        self.estados = self.campos[1].split(', ')   # DEFININDO LISTA DE ESTADOS
        self.estados_finais = self.campos[3].split(', ')  # LISTA DE ESTADOS FINAIS
        self.pilha = self.campos[4].split(', ')   # LISTA DE SIMBOLOS DE PILHA

        self.estado_incial = self.campos[2].split(', ')   # RESOLVENDO PROBLEMA DO ESTADO INCIAL JUNTO COM "D"
        self.estado_incial.remove('D')
        for i in self.estado_incial:
            if i == '':   # MAIS ELEMENTOS INUTEIS '-'
                self.estado_incial.remove(i)

        self.estado_atual = self.estado_incial[0]  # O ESTADO ATUAL SERÁ IGUAL AO ESTADO INICIAL

        print(self.campos)

        for i in self.estados:  # CRIANDO OS NOS DO AUTOMATO DE ACORDO COM OS ESTADOS E ADICIONANDO À LISTA DE MODULOS
            NO = no.No(i)   # PASSANDO O NOME DO NO PARA O CONSTRUOTR DA CLASSE
            self.modulos.append(NO)


    #def setprod(self, rea_de_prod: list): #DEFININDO AS REGRAS DE PRODUÇÃO



    #def processa(self, estado, simbolo):
        #TODO est_atual -> est_destino



