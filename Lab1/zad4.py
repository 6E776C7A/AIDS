list=[1,2,3,4,5,6,7,8,9]
x = 3
y = 0
#IndexError
try:
    print(list[9])
except  IndexError:
    print("Wystąpił IndexError - przekroczyłeś zakres listy")
    pass #Ignoruje wyjątek aby kod mógł się dalej wykonać
#ZeroDivisionError
try:
    z = x/y
except ZeroDivisionError:
    print("Wystąpił ZeroDivisionError - nie dzieli się przez zero")
    pass
#NameError
try:
    print(lista[8])
except NameError:
    print("Wystąpił IndexError - nazwa listy którą chcesz wyświeliić jest niepoprawna")
    pass

