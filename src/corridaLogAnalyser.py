import sys
import re
from Utils import Utils
from Corrida import Corrida
from domain import Piloto, Volta

def buscar_linhas(corrida, nome_arquivo):
    with open(nome_arquivo, "rb") as arq:
        for linha in arq.readlines():
            linha_cln = linha.replace('\xe2', '-')
            match_obj = re.match(r'([0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3})[ |\t]+([0-9]{3}) -.+([A-Z][\.][A-Z]+)[ |\t]+([1-4])[ |\t]+([0-9]{1,2}:[0-9]{2}\.[0-9]{3})[ |\t]+([0-9]+$|([0-9]+,[0-9]{1,3})$)', linha_cln)
            if match_obj:
                tratar_linha(corrida, match_obj)

def tratar_linha(corrida, match_obj):
    utils = Utils()
    piloto = extrair_dados_piloto(corrida, match_obj)
    extrair_dados_volta(corrida, piloto, match_obj)

def extrair_dados_piloto(corrida, match_obj):
    codigo_piloto = int(match_obj.group(2))
    nome_piloto = str(match_obj.group(3))
    piloto_pesq = corrida.pilotoService.procurar_piloto(codigo_piloto)
    piloto = None
    if len(piloto_pesq) > 0:
        piloto = piloto_pesq[0]
    else:
        piloto = Piloto.Piloto(codigo_piloto, nome_piloto)
        corrida.pilotoService.cadastrar_piloto(piloto)
    return piloto
    
def extrair_dados_volta(corrida, piloto, match_obj):
    utils = Utils()
    hora_volta = utils.converter_string_para_hora_volta(match_obj.group(1))
    numero_volta = int(match_obj.group(4))
    tempo_volta = utils.converter_string_para_tempo_volta(match_obj.group(5))
    vel_media = float(match_obj.group(6).replace(',', '.'))
    volta = Volta.Volta(hora_volta, piloto, numero_volta, tempo_volta, vel_media)
    corrida.voltaService.cadastrar_volta(volta)

def executar(corrida, nome_arquivo):
    buscar_linhas(corrida, nome_arquivo)
    corrida.buscar_voltas_por_piloto()
    if corrida.is_corrida_encerrada():
        corrida.montar_grid_chegada()

if len(sys.argv) == 2:
    nome_arquivo = sys.argv[1]
    corrida = Corrida()
    executar(corrida, nome_arquivo)