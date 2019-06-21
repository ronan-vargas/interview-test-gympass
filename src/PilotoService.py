from PilotoRepository import PilotoRepository

class PilotoService:
    def __init__(self):
        self.piloto_repository = PilotoRepository()
    
    def procurar_piloto(self, cod_piloto):
        return self.piloto_repository.procurar_piloto(cod_piloto)

    def cadastrar_piloto(self, piloto):
        return self.piloto_repository.cadastrar_piloto(piloto)

    def buscar_todos_pilotos(self):
        return self.piloto_repository.buscar_todos_pilotos()    