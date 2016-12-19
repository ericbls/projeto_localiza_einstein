# -*- coding: utf-8 -*-

import iwlist
import json
from time import sleep

arquivo = open('banco_dados_dicionario','r')

dict_dados = json.load(arquivo)

x = 1

while (x == 1):

    escaneamento = iwlist.scan('wlp3s0')
    cell = iwlist.parse(escaneamento)

    dict_scan = dict()

    for roteador in cell:
        dict_scan[str(roteador['mac'])] = int(roteador['db'])

    dict_pts = dict()

    for local in dict_dados:

        pontos_local = 0

        for rot_scan in dict_scan:
            if rot_scan not in dict_dados[local]:
                pontos_local += -1
            else:
                if (min(dict_dados[local][rot_scan]) < dict_scan[rot_scan]) and (dict_scan[rot_scan] < max(dict_dados[local][rot_scan])):
                    pontos_local += 1

        dict_pts[local] = pontos_local

    #Organizando um print mais amigável
    print dict_pts

    lista_locais = list()
    lista_pts = list()

    for local in dict_pts:
        lista_locais.append(local)
        lista_pts.append(dict_pts[local])

    print lista_pts
    print lista_locais

    mais_provavel_local = list()
    mais_provavel_pts = list()

    for n in range(0,5):
        indice = lista_pts.index(max(lista_pts))
        top_pts = lista_pts.pop(indice)
        top_local = lista_locais.pop(indice)
        mais_provavel_pts.append(top_pts)
        mais_provavel_local.append(top_local)

    print mais_provavel_pts
    print mais_provavel_local

    for (local, pts) in zip(mais_provavel_local,mais_provavel_pts):
        print ('local {0}: pts {1}'.format(local,pts))

    x = int(raw_input('Continuar: '))

arquivo.close()

