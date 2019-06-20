

class No:

    estado_inicial = ""
    estado_destino = []
    simbolos = []

    def __init__(self, ei, dest, simb):
        self.estado_inicial = ei
        self.estados_destino = dest[::]
        self.simbolos = simb[::]

