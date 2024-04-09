#MyModule

import math

class NieTrojkat(Exception):
    def __init__(self):
        self.message = "Dla podanych długości boków to nie jest trójkąt"

class circle:
    def __init__(self, r):
        self.r = r
    def pole(self):
        pole = math.pi*(self.r*self.r)
        print("Pole koła: ", pole)
    def obwod(self):
        obwod = 2*math.pi*self.r
        print("Obwod koła: " ,obwod)
class square:
    def __init__(self,a):
        self.a = a
    def pole(self):
        pole = self.a*self.a
        print("Pole kwadratu: ", pole)
    def obwod(self):
        obwod = 4*self.a
        print("Obwod kwadratu: ", obwod)
class triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        if (abs(b-c) < a and a < (b+c)):
            print("To jest trójkąt")
        else:
            raise NieTrojkat()
    def obwod(self):
        obwod = self.a + self.b + self.c
        print("Obwod trójkąta: ", obwod)
    def pole(self):
        p = (self.a + self.b + self.c) / 2
        pole = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print("Pole trójkąta: ", pole)