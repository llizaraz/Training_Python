import os
import json
Datos = {'nombre' : 'N/A', 'edad' : 1, 'cursos': ['','',''] }

file = open("lab6a.txt", "w")
file.write("Primera línea" )
file.write("Segunda línea")
file.write(str(Datos))
file.close()



file1 = open("lab6a.txt", 'r')
text = file1.read()
file1.close()

print (text)