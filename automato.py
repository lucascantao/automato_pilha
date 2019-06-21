

class Automato:

    simbolos = []
    estados = []
    estado_incial = []
    estados_finais = []
    estado_atual: str
    pilha = []

    campos = []

    def __init__(self, gramatica: str):

        gramatica = gramatica.replace('(', '')
        gramatica = gramatica.replace(')', '')
        gramatica = gramatica.replace('{', '|')
        gramatica = gramatica.replace('}', '|')
        self.campos = gramatica.split('|')

        for i in self.campos:
            if i == '' or i == ', ':
                self.campos.remove(i)

        self.simbolos = self.campos[0].split(', ')
        self.estados = self.campos[1].split(', ')
        self.estados_finais = self.campos[3].split(', ')
        self.pilha = self.campos[4].split(', ')

        self.estado_incial = self.campos[2].split(', ')   #RESOLVENDO PROBLEMA DO ESTADO INCIAL JUNTO COM "D"
        self.estado_incial.remove('D')
        for i in self.estado_incial:
            if i == '':
                self.estado_incial.remove(i)


        self.estado_atual = self.estado_incial[0]

        print(self.campos)


        #def processa(self, estado, simbolo):
            #TODO est_atual -> est_destino

