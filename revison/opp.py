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

    def get_age(self):
        return self.__age


    def get_obj_typ(self):
        print("Team")

    def tostring(self):
         return "{} is {} and he scored {} at the age of {}".format(self.__player,
                                                                    self.__type,
                                                                    self.__score,
                                                                    self.__age)


ind = team("Virat", "batsman", 121, 27)

print(ind.tostring())

class Ipl(team):
    __owner=""

    def __init__(self,player,type,score, age, owner):
        self.__owner=owner
        super(Ipl,self).__init__(player, type,score,age)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owmer(self):
        return self.__owner

    def tostring(self):
        return "Team owned by {} where {} played as {} and scored {} runs at the age of {}".format(self.__owner,
                                                                                                   self.get_player(),
                                                                                                   self.get_type(),
                                                                                                   self.get_score(),
                                                                                                   self.get_age())
    def make_sound(self,howmany_times=None):
        if howmany_times is None:
            print(self.get_owmer())
        else:
            print(self.get_owmer())
            print("age is", self.get_age())


kkr = Ipl("kohli","batsman",122,27,"SRK")
print(kkr.tostring())
kkr.make_sound(4)
kkr.make_sound()