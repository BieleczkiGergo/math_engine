#!/bin/python3
#This file is for defining the methods and classes

from typing import Type

from numpy import exp


ADDITION = True
MULTIPLICATION = False

#mElement (math element... how creative...) is the main element we will be working with
class mElement:
    #The most important variable is the base, which is, hovewer surprising, the base
    #of the mElement. It can either store an integer, a character, or a list of mElements.
    #(Only having one mElement would serve little purpouse)
    #In the case that it holds an mElement, the type variable comes into play. It will
    #determine if the mElement is an addition or a multiplication
    __slots__ = ("exp", "den", "base", "expType", "denType", "baseType", "cType")

    def __init__(self, base, cType=ADDITION, exp=1, den=1):
        self.base = base
        self.cType = cType
        self.exp = exp
        self.den = den
        self.denType = type(den)
        self.expType = type(exp)
        self.baseType = type(base)

    def __eq__(self, other):
        #if self.base == other.base and self.den == other.den and self.exp == other.exp and self.type == other.type:
        #   return True
        if type(self.base) == type(other.base):
            if type(self.base) == int:
                if type(self.den) == type(other.den):
                    if type(self.den) == int:
                        if type(self.exp) == type(other.exp):
                            if type(self.exp) == int:
                                return self.count() == other.count()
                            elif type(self.exp) == str:
                                return self.exp == other.exp
                            else:
                                return False
                        
                        
        else:
            return False


        return False

    def count(self):
        return (self.base / self.den) ** self.exp

    def countable(self):
        pass

element1 = mElement(base=4, den=4, exp="x")
element2 = mElement(base=3, den=3, exp="x")

print(element1 == element2)
print(type(element1))