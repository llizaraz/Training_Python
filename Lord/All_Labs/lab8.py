import os

lab8 = """Un Administrador Necesita crear un archivo donde solo tenga las direcciones  MAC segun el comando show mac-address Table"""


file1 = open("lab8_input.txt", 'r')
text = file1.read()
file1.close()

#print (text)
print (type(text)) # <class 'str'>

list_mac = text.splitlines() #<class 'list'>  Se esta convirtiendo a una lista haciendo slipt por Lineas
#list_mac = ['ALL   0000.0000.0000  STATIC   CPU']

print (type(list_mac))
#print (list_mac)

"""
for pollo in list_mac:
    # pollo = 2520  0008.2f7d.ba3f  DYNAMIC  Te0/0/24.Efp2520
    pollo1 = pollo.split(' ')
    print (pollo)
    print (pollo1)
    #print(pollo.split(' ')[2])

"""


##############################Ejemplo FOR#####################################################

"""
print (len(list_mac))

print (list_mac[2].split(' ')[3])


for mac in list_mac:
    print (mac.split(' ')[3])

"""



###############################Ejemplo While#############################################
count = 0
print (len(list_mac))

print (list_mac[count])

while count < len(list_mac): #125
    print ('Count :',count  + 1, '/ ' , len(list_mac), ': ', list_mac[count])
    #print ()
    count = count + 1




