from VoltaRepository import VoltaRepository
class VoltaService:
    def __init__(self):
        self.volta_repository = VoltaRepository()
    
    def procurar_voltas_piloto(self, piloto):
        return self.volta_repository.procurar_voltas_piloto(piloto)

    def cadastrar_volta(self, volta):
        return self.volta_repository.cadastrar_volta(volta)    