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



numero = 0
while numero < len(list_mac):
    print ('*' * 10, 'MAC' , list_mac[numero].split(' ')[2] , '*' * 10, )
    print (list_mac[numero].split(' ')[-1])
    valor = numero / len(list_mac)
    print (round(valor * 100),'%')
    numero = numero + 1
