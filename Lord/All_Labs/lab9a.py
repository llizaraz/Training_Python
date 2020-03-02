import os,pprint

text = 'S        190.86.176.72/29 [1/0] via 10.152.56.33'

# Splits at space
print(text.split())

print ('Show ip route ', (text.split()[-1]))

word = 's, 190.86.176.72/29, [1/0], 10.152.56.33'

# Splits at ','
print(word.split(', '))

word = '190.1.1.1:23'

# Splitting at ':'
print(word.split(':'))

