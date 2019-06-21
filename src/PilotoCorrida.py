from datetime import timedelta
from PilotoCorridaAggregate import PilotoCorridaAggregate
class PilotoCorrida:
    def __init__(self, pilotos, voltas_por_piloto):
        self.pilotos = pilotos
        self.voltas_por_piloto = voltas_por_piloto

    def buscar_velocidade_media_piloto(self, tempos_voltas, medias_voltas, tempo_total):
        base_calc = 0
        i = 0
        for tempo_volta in tempos_voltas:
            base_calc += (tempo_volta.total_seconds() / tempo_total.total_seconds()) * medias_voltas[i]
            i += 1
        return base_calc      

    def agregar(self):
        self.aggs = []
        for piloto in self.pilotos:
            voltas = self.voltas_por_piloto[piloto.codigo]
            num_voltas = len(voltas)
            tempo_total = timedelta()
            melhor_volta = None
            tempos_voltas = []
            vel_medias_voltas = []
            if num_voltas > 0:
                for volta in voltas:
                    tempo_total += volta.tempo
                    tempos_voltas.append(volta.tempo)
                    vel_medias_voltas.append(volta.vel_media)
                melhor_volta = min(tempos_voltas)
                vel_media_piloto = self.buscar_velocidade_media_piloto(tempos_voltas, vel_medias_voltas, tempo_total)      
                agg = PilotoCorridaAggregate(piloto, num_voltas, tempo_total, melhor_volta, vel_media_piloto)
                self.aggs.append(agg) 

    def montar_grid_chegada(self):
        grid = sorted(self.aggs, key = lambda x : (x.num_voltas * -1, x.tempo_total))
        vencedor = grid[0]
        pos = 1
        melhores_voltas = []
        for item_grid in grid:
            diff = self.buscar_str_diff_vencedor(vencedor, item_grid)
            print('{} {} {} {} {} {} {} {}'.format(str(pos).zfill(2), str(item_grid.piloto.codigo).zfill(3), item_grid.piloto.nome, item_grid.num_voltas, item_grid.tempo_total, item_grid.melhor_volta, item_grid.vel_media, diff))
            melhores_voltas.append(item_grid.melhor_volta)
            pos += 1
        print('melhor_volta_corrida: {}'.format(min(melhores_voltas)))

    def buscar_str_diff_vencedor(self, vencedor, outro):
        diff_voltas = vencedor.num_voltas - outro.num_voltas
        if diff_voltas > 0:
            return '+{} VOLTA(S)'.format(diff_voltas)
        else:    
            return '+{}'.format(outro.tempo_total - vencedor.tempo_total)