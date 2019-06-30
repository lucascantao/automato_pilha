
class Automato:

    mov_vazio: bool

    # ESPECIFICAÇOES DO AUTOMATO
    simbolos = []
    estados = []
    estado_incial = []
    estados_finais = []
    estado_atual: str
    simbolos_pilha = []

    PILHA= []

    regras_de_prod = []

    def check_automato_vazio(self, rdp: list):
        for line in rdp:
            prod = line.split(", ")
            if (prod[1] and prod[2]) == '-':
                self.mov_vazio = True

        self.mov_vazio = False

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

    def check_pilha_vazia(self):
        if self.PILHA == []:
            return True
        else:
            return False

    def process_vazio(self):
        return

    def processa_simbolo(self, simbolo, equilibrio: bool):

        if simbolo not in self.simbolos:  # checa se o simbolo existe no alfabeto
            print("Símbolo = '%s' não reconhecido" % simbolo)
            return "error"

        if equilibrio:

            for line in self.regras_de_prod:  # checa qual estado lê o vazio
                prod = line.split(', ')

                if self.estado_atual == prod[0] and prod[1] == '-':

                    self.estado_atual = prod[3]  # atualizando estado atual

                    if self.PILHA != [] and prod[2] == self.PILHA[-1]:
                        self.PILHA.pop((len(self.PILHA))-1)
                    elif prod[2] == '-':
                        pass
                    else:
                        print("&( %s, %s, %s ) : ERRO!!!" % (prod[0], prod[1], prod[2]))
                        print("Simbolo não exite na pilha: '%s'" % prod[2])
                        return "error"

                    if prod[4] == '-':
                        pass
                    else:
                        self.PILHA.append(prod[4])

                    print("&( %s, %s, %s ) : (%s, %s) | " % (prod[0], prod[1], prod[2], prod[3], prod[4]), self.PILHA)

                    # return "simbolo_lido"

        for line in self.regras_de_prod:  # checa qual estado ler o simbolo atual
            prod = line.split(', ')

            if self.estado_atual == prod[0] and simbolo == prod[1]:

                self.estado_atual = prod[3]  # atualizando estado atual

                if self.PILHA != [] and prod[2] in self.PILHA[-1]:
                    self.PILHA.pop((len(self.PILHA))-1)
                elif prod[2] == '-':
                    pass
                else:
                    print("&( %s, %s, %s ) : ERRO!!!" % (prod[0], prod[1], prod[2]))
                    print("Simbolo não exite na pilha: '%s'" % prod[2])
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

    def processa_palavra(self, palavra: str):

        # VARIÁVEIS DE CONTROLE
        contador_de_simbolos = 0
        unidade = 1
        equilibrio = False

        print("\n", palavra, "\n")

        for s in palavra:

            contador_de_simbolos += unidade

            if contador_de_simbolos > int((len(palavra))/2):
                equilibrio = True  # Se passou da metade da palavra...

            status = self.processa_simbolo(s, equilibrio)

            if equilibrio:  # Depois que o vazio é lido, a checagem não é mais necessária e "equilíbrio" volta para False.
                contador_de_simbolos, unidade = 0, 0  # As variáveis de incremento são zeradas, assim "equilíbrio" não se torna mais True
                equilibrio = False

            if status == "error":
                print("RECUSADA")
                return

            if status == "pilha_vazia":
                print("ACEITA")
                return

        else:

            for s in palavra:
                status = self.process_vazio()

        for line in self.regras_de_prod:  # quando a palavra terminar, ver se o estado atual checa a pilha vazia
            prod = line.split(', ')

            if self.estado_atual == prod[0] and prod[1] == '?':
                vazia = self.check_pilha_vazia()
                if vazia:
                    self.estado_atual = prod[3]  # se vazia, atualiza o estado atual
                    if self.estado_atual in self.estados_finais:  # se chegar ao estado final, aceita
                        print("&( %s, %s, %s ) : (%s, %s) | " % (prod[0], prod[1], prod[2], prod[3], prod[4]),
                              self.PILHA)
                        print("ACEITA")
                        return
                    else:
                        print("RECUSADA")
                        return
                else:
                    print("Pilha não vazia")
                    return

        print("RECUSADA")