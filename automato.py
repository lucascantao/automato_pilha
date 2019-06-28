import no


class Automato:

    first_intetaration = True


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

    def check_pilha_vazia(self):
        if self.PILHA == []:
            return True
        else:
            return False

    def process(self, simbolo):

        if simbolo not in self.simbolos:  # checa se o simbolo existe no alfabeto
            print("Símbolo = '%s' não reconhecido" % simbolo)
            return "error"

        for line in self.regras_de_prod:  # checa qual estado ler o simbolo atual
            prod = line.split(', ')

            if self.estado_atual == prod[0] and simbolo == prod[1]:

                self.estado_atual = prod[3]  # atualizando estado atual

                # if self.first_intetaration:
                #     self.first_intetaration = False  # na primeira interação não a leitura de pilha
                # else:

                if prod[2] in self.PILHA:
                    self.PILHA.remove(self.PILHA[-1])
                elif prod[2] == '-':
                    pass
                else:
                    print("&( %s, %s, %s ) : ERRO!!!"%(prod[0], prod[1], prod[2]))
                    print("Simbolo não exite na pilha: '%s'"%prod[2])
                    return "error"

                if prod[4] == '-':
                    pass
                else:
                    self.PILHA.append(prod[4])

                print("&( %s, %s, %s ) : (%s, %s) | " % (prod[0], prod[1], prod[2], prod[3], prod[4]), self.PILHA)

                return "simbolo_lido"

        for line in self.regras_de_prod:  # se o estado atual não ler o simbolo, ver se ele checa a pilha vazia
            prod = line.split(', ')

            if self.estado_atual == prod[0] and simbolo == '?':
                vazia = self.check_pilha_vazia()
                if vazia:
                    self.estado_atual = prod[3]  # se vazia, atualiza o estado atual
                    if self.estado_atual in self.estados_finais:  # se chegar ao estado final, aceita
                        return "pilha_vazia"
                    else:
                        return "error"
                else:
                    print("Pilha não vazia")
                    return "error"

        return "error"

    def proc_pal(self, palavra: str):
        print("\n", palavra, "\n")
        for s in palavra:

            status = self.process(s)

            if status == "error":
                print("Palavra não aceita")
                return

            if status == "pilha_vazia":
                print("palavra acaita")
                return

        for line in self.regras_de_prod:  # ver se ele checa a pilha vazia
            prod = line.split(', ')

            if self.estado_atual == prod[0] and prod[1] == '?':
                vazia = self.check_pilha_vazia()
                if vazia:
                    self.estado_atual = prod[3]  # se vazia, atualiza o estado atual
                    if self.estado_atual in self.estados_finais:  # se chegar ao estado final, aceita
                        print("&( %s, %s, %s ) : (%s, %s) | " % (prod[0], prod[1], prod[2], prod[3], prod[4]),
                              self.PILHA)
                        print("palavra aceita")
                        return
                    else:
                        print("palavra não aceita")
                        return
                else:
                    print("Pilha não vazia")
                    return "error"

