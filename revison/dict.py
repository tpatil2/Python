import os
import sys
import random

# dictionary consist of keys and values

my_gpa ={ 'CSCI340': '4.0',
          'CSCI311': '0.0',
          'CSCI640': '3.9',
          'CSCI567': '3.3',
          'CSCI546': '3.95',}

print(my_gpa['CSCI340'])
print(my_gpa.keys())
print(my_gpa.values())

my_gpa['CSCI311'] = '3.8'
del my_gpa['CSCI311']
print(my_gpa.values())
