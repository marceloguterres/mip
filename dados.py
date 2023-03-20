#!/usr/bin/python
# coding=utf8

"""
 +-------------+
 |  D A D O S  |
 +-------------+

Script Auxiliar para carregar dados para o projeto
Avaliação de Impactos da Infraesrutura Aeroportuária
SAC | ITA

Default: bucket S3 mantido por Mauro Zac
ou especificar path para acessar dados localmente
"""

__version__ = "v.1.5 | 2023."


import json

import requests
import pandas as pd


def carregar_mip_nereus(ano=2015, path=""):
    """Carrega as matrizes insumo produtos de 2010 a 2018.
    fonte dos dados: matriz SxS NEREUS-USP formatada em econodata
    https://econodata.s3.amazonaws.com/Nereus/mip68br2010.csv
    retorna dataFrame do ano especificado
    """
    url = "https://econodata.s3.amazonaws.com/"
    res = "Nereus/mip68br"
    if path: 
    	url = path
    ano = str(ano)
    anos = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
    if ano not in anos:
        raise Exception('[!!] Matriz para '+ano+' não está disponível')
    mip = pd.read_csv(url+res+ano+".csv", index_col=0)
    if path:
        print('[~~] Carregada MIP SxS Brasil | Nereus USP | ' + ano)
    else:
        print('[s3] Carregada MIP SxS Brasil | Nereus USP | ' + ano)
    return mip


def carregar_qls(ano=2018, path=""):
    """Carrega dataframe dos quocientes locaciomais do ano.
    Precisa estar consistente com o método de regionalização.
    """
    url = "https://econodata.s3.amazonaws.com/"
    res = "Regional/ql"+str(ano)+".csv"
    if path:
        print('[~~] Tabela de Quocientes Locacionais')
        qls = pd.read_csv(path+res, dtype={'utps':str})
        qls.set_index('utps', inplace=True)
    else:
        print('[s3] Tabela de Quocientes Locacionais')
        qls = pd.read_csv(url+res, dtype={'utps':str})
        qls.set_index('utps', inplace=True)

    return qls


def carregar_pop(ano=2018, path=""):
    """Carrega tabela de dados com proporções da poplução no ano e 
    valores adicionados.
    Precisa estar consistente com o método de regionalização.
    """
    url = "https://econodata.s3.amazonaws.com/"
    res = "Regional/pop"+str(ano)+".csv"
    if path:
        print('[~~] Tabela de População e VA')
        pop = pd.read_csv(path+res, dtype={'utps':str})
        pop.set_index('utps', inplace=True)
    else:
        print('[s3] Tabela de População e VA')
        pop = pd.read_csv(url+res, dtype={'utps':str})
        pop.set_index('utps', inplace=True)
    return pop


def carregar_utp(path=""):
    """Carrega tabela de dados com identificação das UTPs
    """
    url = "https://econodata.s3.amazonaws.com/"
    res = "Regional/utps.csv"
    if path:
        print('[~~] Tabela de UTPs')
        utp = pd.read_csv(path+res, dtype={'utps':str})
        utp.set_index('utps', inplace=True)
    else:
        print('[s3] Tabela de UTPs')
        utp = pd.read_csv(url+res, dtype={'utps':str})
        utp.set_index('utps', inplace=True)
    return utp


def carregar_atividades68(path=""):
    url = "https://econodata.s3.amazonaws.com/"
    res = "Chaves/atividadesMip68.json"
    if path:
        print('[~~] Códigos e descrição das atividades para MIP 68')
        with open(path+res) as f: 
            atividades = json.loads(f.read())
    else:
        print('[s3] Códigos e atividades para MIP 68')
        atividades = json.loads(requests.get(url+res).text)
    cods68 = atividades["codigos_atividades_68"]
    labels68 = atividades["labels_atividades_68"]
    mapa = {}
    for i in range(len(cods68)):
        mapa[cods68[i]] = labels68[i]
    return cods68, labels68, mapa


def carregar_compatibiliza_atividades_a_3(path=""):
    """Carrega referencia para compatibilizar 68 atividades nos 3 grandes setores
    """
    url = "https://econodata.s3.amazonaws.com/"
    res = "Chaves/compatibiliza68a03.json"
    if path:
        print('[~~] Compatibilização 68 atividades em 3 setores')
        with open(path+res) as f:
            compa = json.loads(f.read())
        return compa
    compa = json.loads(requests.get(url+res).text)
    print('[S3] Compatibilização 68 atividades em 3 setores')
    return compa

