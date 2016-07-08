import random
import sys
import os


# if else elif    ==  < > <= >=
# logical conditions and or not

age=17

if age>21:
    print('you can Marry')
else:
    print('you dont')


if age < 16:
    print('you cant drive')
elif age > 21:
    print('you can drive with your wife')
else:
    print("wait for", 21 - age, "years more")

if((age > 16)and(age >= 21)):
    print('you can drive as wll as u can marry')
elif((age < 16)and (age > 9)):
    print('you are in school')
elif not(age>25):
    print('you will be charged under age fees')
else:
    print('none of these')
