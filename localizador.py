import iwlist
import time
import json

arquivo = open('/home/ericlee/Downloads/banco_dados_dicionario','r')

dados = json.load(arquivo)

print(type(dados))

x = 1

while (x == 1):

    scan = iwlist.scan('wlps30')
    cell = iwlist.parse(scan)

    dict_chances = dict()

    for local in dados:
        chance = 0
        for roteador in dados[local]:
            sinal = dados[local][roteador]
            
            
        
    time.sleep(2)
    print ('aiai')
    x=0

arquivo.close()
