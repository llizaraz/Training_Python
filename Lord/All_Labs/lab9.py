import os,pprint


file1 = open("lab8_input.txt", 'r')
text = file1.read()
file1.close()

#print (text)
print (type(text)) # <class 'str'>

list_mac = text.splitlines() #<class 'list'>  Se esta convirtiendo a una lista haciendo slipt por Lineas
#list_mac = ['ALL   0000.0000.0000  STATIC   CPU']

print (type(list_mac))
#print (list_mac[2])


print (list_mac[-1])

##############################Ejemplo FOR##############################

valores = []
#while count



for mac in list_mac:
    #print (mac)
    # mac = '1002  3cce.730f.e041  DYNAMIC  Te0/0/24.Efp1
    Datos = {'IP': None, 'MAC': None, 'Vlan': None, 'Intf': None}
    mac = mac.split(' ')
    #print (mac)
    # mac = ['ALL', '', '', '0000.0000.0000', '', 'STATIC', '', '', 'CPU']
    Datos.update({'MAC': mac[2], 'Vlan': mac[0], 'Intf': mac[6]})
    valores.append(Datos)

#print (valores)
pprint.pprint(valores)

