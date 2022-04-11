import os
import shutil
from threading import Timer
from layout import chama_profissional

PASTA_FILA = 'worker/fila'

def verifica_arquivos():
    quantidade = 0
    for arquivo in os.listdir(PASTA_FILA):
        with open(f'{PASTA_FILA}/{arquivo}', 'r') as f:
            for linha in f:
                pro = chama_profissional(linha)
                print('{} atendendo cliente {} no dia {} na localidade {}'.format(
                    pro.__class__.__name__, pro.cli_id, pro.dt_req, pro.coords
                ))
            quantidade += 1
        shutil.move(f'{PASTA_FILA}/{arquivo}', f'worker/processados/{arquivo}')
    print(f'Arquivos processados: {quantidade}')
    Timer(3, verifica_arquivos).start()  # --- Repete a cada 3 segundos ---


verifica_arquivos()