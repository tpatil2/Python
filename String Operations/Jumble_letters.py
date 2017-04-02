import random

string  = "This not jumbled string"
jumbled=""


print(string)
string = list(string)
print(string)

for letter in range(0, len(string)):
    jumbled+= string.pop(random.randint(0,len(string)-1))
    print(jumbled)


'''
OUTPUT
This not jumbled string
['T', 'h', 'i', 's', ' ', 'n', 'o', 't', ' ', 'j', 'u', 'm', 'b', 'l', 'e', 'd', ' ', 's', 't', 'r', 'i', 'n', 'g']
o
or
orl
orlj
orljn
orljnt
orljnte
orljnteT
orljnteT
orljnteT
orljnteT  u
orljnteT  ut
orljnteT  ut
orljnteT  ut m
orljnteT  ut mb
orljnteT  ut mbd
orljnteT  ut mbdi
orljnteT  ut mbdig
orljnteT  ut mbdigi
orljnteT  ut mbdigih
orljnteT  ut mbdigihs
orljnteT  ut mbdigihsn
orljnteT  ut mbdigihsns

Process finished with exit code 0
'''