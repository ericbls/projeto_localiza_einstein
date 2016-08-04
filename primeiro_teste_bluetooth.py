# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 17:07:19 2016
"""

from pybluez import bluetooth

target_name = "My Phone"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
else:
    print "could not find target bluetooth device nearby"
    
#Entendo que o código localiza apenas o sinal bluetooth do dispositivo com o endereço que eu designar em 
# target_address. E atualmente o código está como "None", precisando ser substituído pelo endereço de algum
#dispositivo. Contudo, o problema não está aí, mas sim em "No module named pybluez".