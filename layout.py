from prestadores import (
    profissional, marceneiro,
    chaveiro, eletricista,
    encanador, mecanico_auto
)

CLASSES = {
    '1003': marceneiro.Marceneiro,
    '2018': chaveiro.Chaveiro,
    '3109': eletricista.Eletricista,
    '4066': encanador.Encanador,
    '5321': mecanico_auto.MecanicoAuto        
}


def chama_profissional(linha: str) -> profissional.Profissional:
    codigo = linha[:4]
    dt_req = linha[4:12]
    cli_id = linha[12:15]
    coords = linha[15:23]
    return CLASSES[codigo](dt_req, cli_id, coords)
