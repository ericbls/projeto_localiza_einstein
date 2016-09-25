import iwlist
import json

arquivor = open('/home/ericlee/Downloads/banco_dados_dicionario','r')

scan = iwlist.scan('wlp3s0')
cell = iwlist.parse(scan)

dicionario=json.load(arquivor)

arquivor.close()

arquivow = open('/home/ericlee/Downloads/banco_dados_dicionario','w')

local = raw_input('Insira o nome do local medido: ')

if local in dicionario:
    
    for i in cell:
        if i['mac'] in dicionario[local]:
            dicionario[local][i['mac']].append(int(i['db']))
            
        else:
            dicionario[local][i['mac']] = [int(i['db'])]
    
else:
    dicionario[local]=dict()
    
    for i in cell:
        dicionario[local][i['mac']] = [int(i['db'])]

salvar = json.dumps(dicionario)

arquivow.write(salvar)

arquivow.close()
