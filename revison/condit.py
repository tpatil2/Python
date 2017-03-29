import os
import sys
import random

age = 12


if age == 16:
    print("you are old enough to drive car")
elif age > 21:
    print("you are old enough to drove truck")
else:
    print("you are not old enough to drive car")



# and or not

if (age >= 16 and age >21):
    print("you can drive car and truck both")
elif (age > 16 and not(age>21)):
    print("you can drive only car but not truck")
elif not(age>=16):
    print("you can not drive")
