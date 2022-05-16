#/bin/python3
#This file is for defining the methods and classes

ADDITION = True
MULTIPLICATION = False

#mElement (math element... how creative...) is the main element we will be working with
class mElement:
    #The most important variable is the base, which is, hovewer surprising, the base
    #of the mElement. It can either store an integer, a character, or a list of mElements.
    #(Only having one mElement would serve little purpouse)
    #In the case that it holds an mElement, the type variable comes into play. It will
    #determine if the mElement is an addition or a multiplication
    __slots__ = ("exp", "den", "base", "type", "expType", "denType", "baseType")

    def __init__(self, base, type=ADDITION, exp=1, den=1):
        self.base = base
        self.type = type
        self.exp = exp
        self.den = den
        self.baseType = type(self.base)
        

    def __eq__(self, other):
        #if self.base == other.base and self.den == other.den and self.exp == other.exp and self.type == other.type:
        #   return True
        if self.type == other.type:
            if self.base == other.base:
                if self.exp == other.exp:
                    if self.den == other.den:
                        return True


        return False


element1 = mElement(4)
element2 = mElement(3)

print(element1 == element2)
print(type(element1))