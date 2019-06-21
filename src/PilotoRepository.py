class PilotoRepository:
    def __init__(self):
        self.pilotos = []

    def procurar_piloto(self, cod_piloto):
        return [x for x in self.pilotos if x.codigo == cod_piloto]

    def cadastrar_piloto(self, piloto):
        self.pilotos.append(piloto)

    def buscar_todos_pilotos(self):
        return self.pilotos    