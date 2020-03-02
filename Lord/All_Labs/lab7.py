import os
import json

################################Crear 2 Archivos###################
file1 = open("lab7a.txt", "w")
file1.write("File1" )
file1.close()

file2 = open("lab7b.txt", "w")
file2.write("File2" )
file2.close()

################################READ 2 Archivos de Text#############

file1 = open("lab7a.txt", 'r')
text1 = file1.read()
file1.close()

file2 = open("lab7b.txt", 'r')
text2 = file2.read()
file2.close()

print (text1)
print (text2)


################################Crear Final###################
file_final = open("lab7_final.txt", "w")
file_final.write(text1)
file_final.write(text2)
file_final.close()

