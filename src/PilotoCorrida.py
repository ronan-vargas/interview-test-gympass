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

            tempo_total = timedelta()
            tempos_voltas = []
            vel_medias_voltas = []

            if len(voltas) > 0:
                for volta in voltas:
                    tempo_total += volta.tempo
                    tempos_voltas.append(volta.tempo)
                    vel_medias_voltas.append(volta.vel_media)

                melhor_volta = min(tempos_voltas)
                vel_media_piloto = self.buscar_velocidade_media_piloto(tempos_voltas, vel_medias_voltas, tempo_total)      
                agg = PilotoCorridaAggregate(piloto, len(voltas), tempo_total, melhor_volta, vel_media_piloto)
                self.aggs.append(agg) 

    def montar_grid_chegada(self):
        grid = sorted(self.aggs, key = lambda x : (x.num_voltas * -1, x.tempo_total))
        vencedor = grid[0]
        pos = 1
        melhores_voltas = {}
        tma = 0
        self.imprimir_cabecalho()
        for item_grid in grid:
            diff = self.buscar_str_diff_vencedor(vencedor, item_grid)
            tam = self.imprimir_colunas(item_grid, pos, diff)
            melhores_voltas[item_grid.piloto.nome] = item_grid.melhor_volta
            pos += 1
        self.imprimir_rodape(tam)
        piloto_melhor_volta = min(melhores_voltas, key=melhores_voltas.get)
        tempo_melhor_volta = melhores_voltas[piloto_melhor_volta]
        print('Melhor volta da corrida: {} em {}'.format(piloto_melhor_volta, tempo_melhor_volta))

    def imprimir_cabecalho(self):
        linha = []
        linha.append('|POSICAO')
        linha.append('PILOTO'.ljust(31))
        linha.append('VOLTAS'.ljust(6))
        linha.append('TEMPO TOTAL'.ljust(15))
        linha.append('MELHOR VOLTA'.ljust(15))
        linha.append('VEL MEDIA'.ljust(15))
        linha.append('DIFERENCA      |'.ljust(16))
        print('-' * (sum([len(i) for i in linha]) + len(linha)))
        print('|'.join(linha))
        print('-' * (sum([len(i) for i in linha]) + len(linha)))

    def imprimir_colunas(self, item_grid, pos, diff):
        linha = []
        linha.append('|' + str(pos).zfill(2).rjust(7))
        linha.append(str(item_grid.piloto.codigo).zfill(3) + ' - ' + item_grid.piloto.nome.ljust(25))
        linha.append(str(item_grid.num_voltas).rjust(6))
        linha.append(str(item_grid.tempo_total).rjust(15))
        linha.append(str(item_grid.melhor_volta).rjust(15))
        linha.append(str(round(item_grid.vel_media, 3)).rjust(15))
        linha.append(str(diff).ljust(15) + '|')
        linha_str = '|'.join(linha)
        print(linha_str)
        return len(linha_str) 
        

    def imprimir_rodape(self, tam):
        print('-' * tam)

    def buscar_str_diff_vencedor(self, vencedor, outro):
        diff_voltas = vencedor.num_voltas - outro.num_voltas
        if diff_voltas > 0:
            return '+{} VOLTA(S)'.format(diff_voltas)
        else:    
            return '+{}'.format(outro.tempo_total - vencedor.tempo_total)