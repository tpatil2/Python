import os
import sys
import random

class team:
    __player=""
    __type = ""
    __score = 0
    __age = 0

    def __init__(self, player, type, score, age):
        self.__player=player
        self.__type = type
        self.__score = score
        self.__age = age

    def set_player(self,player):
        self.__player = player

    def get_player(self):
        return self.__player



    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type



    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score



    def set_age(self, age):
        self.__age = age

    def get_player(self):
        return self.__age


    def get_type(self):
        print("Team")

    def tostring(self):
         return "{} is {} and he scored {} at the age of {}".format(self.__player,
                                                                    self.__type,
                                                                    self.__score,
                                                                    self.__age)


ind = team("Virat", "batsman", 121, 27)

print(ind.tostring())