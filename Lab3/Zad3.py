import random
import math

def MonteCarlo(function,criteria,rangeX,rangeY,numberOfIterations):
    suma = 0
    for i in range(numberOfIterations):
        x = random.random()*rangeX
        y = random.random()*rangeY
        if criteria(function,x,y):
            suma = suma + 1
    return (suma/numberOfIterations) * rangeX * rangeY

def main():
    criteria_sin = lambda f,x,y: y <= f(x)
    wynik_sin = MonteCarlo(math.sin,criteria_sin,2,2,1000000)
    print("wynik sinusa w zakresie 0 - 2: ", wynik_sin)
    r = input("Podaj promien koła: ")
    criteria_circle = lambda f,x,y: (x-f)**2 + (y-f)**2 <= f*f
    wynik_circle = MonteCarlo(float(r),criteria_circle,2*float(r),2*float(r),1000000)
    print("wynik koła o promieniu r: ", wynik_circle)

if __name__ == '__main__':
    main()