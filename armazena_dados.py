import iwlist
import json

arquivor = open('/home/ericlee/Downloads/banco_dados_dicionario','r')

scan = iwlist.scan('wlp3s0')
cell = iwlist.parse(scan)

dicionario=json.load(arquivor)

arquivor.close()

arquivow = open('/home/ericlee/Downloads/banco_dados_dicionario','w')

local = raw_input('Insira o nome do local medido: ')

while (local in dicionario):
    local = raw_input('Este local ja foi inserido: ')

dicionario[local]=dict()
for i in cell:
    dicionario[local][i['mac']] = int(i['db'])

salvar = json.dumps(dicionario)

arquivow.write(salvar)

arquivow.close()
