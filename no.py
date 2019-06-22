

class No:

    estado_origem = ""
    estado_destino = []
    simbolos = []

    def __init__(self, estado_origem):
        self.estado_origem = estado_origem

    def setNo(self, dest, simb):
        self.estados_destino = dest[::]
        self.simbolos = simb[::]

