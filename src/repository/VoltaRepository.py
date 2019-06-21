class VoltaRepository:
    def __init__(self):
        self.voltas = []

    def procurar_voltas_piloto(self, piloto):
        voltas_piloto = [x for x in self.voltas if x.piloto == piloto]
        return voltas_piloto

    def cadastrar_volta(self, volta):
        self.voltas.append(volta)