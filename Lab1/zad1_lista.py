import time

start = time.time()
L = [1,2]
x = 0
z = 0
y = []
k = 0
#lista L 48 elementów
for i in range(46):
    L.append((L[i]+L[i+1])/(L[i+1]-L[i]))
#policenie sumy elementów potem średniej
for i in range(len(L)):
    x += L[i]
srednia = x/len(L)
print("Średnia to: ")
print(srednia)
#oblicznie mody na podstawie zliczenia unikalnych wartości i zapisania do nowej tablicy
for i in range(len(L)):
    y.append(L.count(L[i]))
if (max(y))==1:
    print("moda to wszystkie wartości")
else:
    z= y.index(max(y)) #w przypadku wystąpienia mody za pomocą indexy wyświetlam wartość mody
    print("moda")
    print(L[z])
#sortowanie wymagane aby sprawdzić czy liczby sie powtarzają
L.sort()
#sprawdzanie powtarzalności liczb
print("Liczby które sie powtarzają: ")
for i in range(len(L)-1):
    if L[i]==L[i+1]:
        print(L[i])
    else:
        k += 1;
        if k==(len(L)-1):
            print ("Liczby sie nie powtarzają")
time.sleep(1) #Wstawiłem sleep bo czasem wynik czasu to 0.0 sekundy
end = time.time()
finish = end - start - 1 #Odelmije sekunde
print('Czas wykonywania programu w sekundach(więcej = gorzej):')
print(finish)