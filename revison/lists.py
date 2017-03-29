import random
import sys
import os


program = ['web', 'mobile', 'system', 'ios', 'linux']

print(program)

print(program[0])

program.append('applicaiton')
program.insert(0,'sys')
program.sort()
program.reverse()
program.remove('ios')
print(program)

del program[4]
print(program)


print(len(program))
print(max(program))
print(min(program))

print('------')


langauge = ['c','C++', 'python','php','shell']
print(langauge)
skill = [program, langauge]
print(skill)
print(skill[1][0])


