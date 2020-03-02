import os

lab8 = """Un Administrador Necesita crear un archivo donde solo tenga las direcciones  MAC segun el comando show mac-address Table"""


file1 = open("lab8_input.txt", 'r')
text = file1.read()
file1.close()

print (text)
print (type(text)) # <class 'str'>

list_mac = text.splitlines() #<class 'list'>  Se esta convirtiendo a una lista haciendo slipt por Lineas
#list_mac = ['ALL   0000.0000.0000  STATIC   CPU']

print (type(list_mac))
print (list_mac[2])

##############################Ejemplo FOR#####################################################

#for mac in list_mac:
#    print (mac)



###############################Ejemplo While#############################################
#count = 0
#while count < len(list_mac):
#    print (list_mac[count])
#    count = count + 1

