import random
import sys
import os

print ("\nHello welcome to python\n")


name = "Tejas Patil"
x=9829023358
print(name,"\n")
print(x,"\n")


print("5+2 =", 5+2,"\n")
print("5/2 =", 5/2)
print("5*2 =", 5*2)
print("5-2 =", 5-2)
print("5**2 =", 5**2)
print("5//2 =", 5//2) # prints only integer part

'''
multiline comment

'''

#order of operation
# **
# */+-
print("6/3+5+1-2*2 =", 2**4/2+5+1-2*2)

print("6/3+(5+1-2)*2 =", 6/3+(5+1-2)*2,'\n')

quote= "\"Hello there\""

multiline_quote='''This is multiline quote'''

print(quote,multiline_quote)

print("This is first line",end='\n'*5)
print("newline")

print("%s %s %s" % ('begin', quote,multiline_quote))