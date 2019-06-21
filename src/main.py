import sys
import re
from Utils import Utils
from Corrida import Corrida
from Piloto import Piloto
from Volta import Volta

def tratar_linha(corrida, match_obj):
    utils = Utils()
    hora_volta = utils.converter_string_para_hora_volta(match_obj.group(1))
    codigo_piloto = int(match_obj.group(2))
    nome_piloto = str(match_obj.group(3))
    numero_volta = int(match_obj.group(4))
    tempo_volta = utils.converter_string_para_tempo_volta(match_obj.group(5))
    vel_media = float(match_obj.group(6).replace(',', '.'))
    piloto_pesq = corrida.pilotoService.procurar_piloto(codigo_piloto)
    if len(piloto_pesq) > 0:
        volta = Volta(hora_volta, piloto_pesq[0], numero_volta, tempo_volta, vel_media)
    else:
        piloto = Piloto(codigo_piloto, nome_piloto)
        corrida.pilotoService.cadastrar_piloto(piloto)
        volta = Volta(hora_volta, piloto, numero_volta, tempo_volta, vel_media)
    
    corrida.voltaService.cadastrar_volta(volta)
def buscar_linhas(corrida, nome_arquivo):
    with open(nome_arquivo, "rb") as arq:
        for linha in arq.readlines():
            linha_cln = linha.replace('\xe2', '-')
            match_obj = re.match(r'([0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3})[ |\t]+([0-9]{3}) -.+([A-Z][\.][A-Z]+)[ |\t]+([1-4])[ |\t]+([0-9]{1,2}:[0-9]{2}\.[0-9]{3})[ |\t]+([0-9]+$|([0-9]+,[0-9]{1,3})$)', linha_cln)
            if match_obj:
                tratar_linha(corrida, match_obj)

if len(sys.argv) == 2:
    nome_arquivo = sys.argv[1]
    corrida = Corrida()
    buscar_linhas(corrida, nome_arquivo)
    corrida.buscar_voltas_por_piloto()
    if corrida.is_corrida_encerrada():
    	corrida.montar_grid_chegada()
