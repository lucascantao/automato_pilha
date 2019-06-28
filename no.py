

class No:

    estado_origem = ""
    estado_destino = []
    simbolos = []
    pilha_read = []
    pilha_write = []

    def __init__(self, estado_origem):
        self.estado_origem = estado_origem

    def setNo(self, simb, read, dest, write):
        self.estado_destino.append(dest)
        self.simbolos.append(simb)
        self.pilha_read.append(read)
        self.pilha_write.append(write)

    def getNo(self):
        return self.estado_origem
