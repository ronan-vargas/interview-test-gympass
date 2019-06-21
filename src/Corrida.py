from service import VoltaService, PilotoService
from PilotoCorrida import PilotoCorrida
class Corrida:
    def __init__(self):
        self.voltaService = VoltaService.VoltaService()
        self.pilotoService = PilotoService.PilotoService()

    def buscar_voltas_por_piloto(self):
        self.voltas_por_piloto = {}
        self.todos_pilotos = self.pilotoService.buscar_todos_pilotos() 
        for piloto in self.todos_pilotos:
            self.voltas_por_piloto[piloto.codigo] = self.voltaService.procurar_voltas_piloto(piloto)
        return self.voltas_por_piloto

    def is_corrida_encerrada(self):
        pilotos_com_corrida_encerrada = [self.voltas_por_piloto[x] for x in self.voltas_por_piloto.keys() if len(self.voltas_por_piloto[x]) == 4]
        return len(pilotos_com_corrida_encerrada) > 0

    def montar_grid_chegada(self):
        pilotoCorrida = PilotoCorrida(self.todos_pilotos, self.voltas_por_piloto)
        pilotoCorrida.agregar()
        pilotoCorrida.montar_grid_chegada()    