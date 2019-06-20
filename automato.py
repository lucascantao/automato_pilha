

class Automato:

    Alfabeto = [] #simbolos
    Q = [] #estados
    D = [] #regras de produção
    S: str #estado inicial
    F = [] #estados finais
    V = [] #Simbolos da Pilha


    def __init__(self, Alfa, Q, D, S, F, V):
        self.Alfabeto = Alfa[::]
        self.Q = Q[::]
        self.D = D[::]
        self.S = S[::]
        self.F = F[::]
        self.V = V[::]

    estado_atual = S

    #def processar_palavra(self, palavra)