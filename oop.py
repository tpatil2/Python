import os
import sys
import random

class Animal:
    #Privare attrubute
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    # constructure
    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    #function inside class for set and get the values

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    #polymorphism

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kg and say {}".format(self.__name,
                                                              self.__height,
                                                              self.__weight,
                                                              self.__sound)


cat = Animal( 'Whiskers',33,10,'Meow')
print(cat.toString())
