import os,pprint


file1 = open("show mac-address-table.txt", 'r')
mac_txt = file1.read()
file1.close()

file1 = open("show arp vrf all location.txt", 'r')
arp_txt = file1.read()
file1.close()


file1 = open("show interface description.txt", 'r')
desc_txt = file1.read()
file1.close()




#print (text)
print (type(arp_txt)) # <class 'str'>

list_mac = mac_txt.splitlines() #<class 'list'>  Se esta convirtiendo a una lista haciendo slipt por Lineas
#list_mac = ['ALL   0000.0000.0000  STATIC   CPU']

list_arp = arp_txt.splitlines()
list_desc = desc_txt.splitlines()
##############################Ejemplo FOR##############################


valores = []

###################################SHOW MAC ADDRESS Table Dynamic #########################
for mac in list_mac:
    mac = mac.split(' ')
    #print (mac)
    #input('Pausa')
    #mac = ['411', '', '00a0.1232.bb00', '', '', 'dynamic', '', 'Yes', '', '', '', '', '', '', '', '370', '', '', 'Gi1/10']
    Datos = {'IP': None, 'MAC': None, 'Vlan': None, 'Intf': None ,'Intf_Description': None}
    Datos.update({'MAC': mac[2], 'Vlan': mac[0], 'Intf': mac[-1]})
    valores.append(Datos)
    #valores =  [{'IP': None,'Intf': 'Gi9/5','Intf_Description': None,'MAC': '0000.5031.c516','Vlan': '424'}]


for arp in list_arp:
    arp = arp.split(' ')
    for mac in valores:
        try:
            if arp[7] == mac['MAC']:
                mac['IP'] = arp[0]
        except:
            pass

for arp in list_arp:
    arp = arp.split(' ')
    #arp = ['10.25.50.1', '', '', '', '', '', '00:01:36', '0040.4384.6afd', 'Dynamic', 'ARPA', 'Bundle-Ether25212.540']
    for mac in valores:
            # mac = {'IP': None,'Intf': 'Gi9/5','Intf_Description': None,'MAC': '0000.5031.c516','Vlan': '424'}
        if mac['MAC'] ==  arp[-4]:
            mac['IP'] = arp[0]

for descr in list_desc:
    print (descr)


#for ip in valores:
#    if ip['IP'] != None:
#        print (ip)

