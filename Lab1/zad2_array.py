from array import *
import time

start = time.time()
L = array('f', [1, 2])
x = 0
z = 0
y = array('f',[])
k = 0

for i in range(46):
    L.append((L[i]+L[i+1])/(L[i+1]-L[i]))

for i in range(len(L)):
    x += L[i]
srednia = x/len(L)
print("Średnia to: ")
print(srednia)

for i in range(len(L)):
    y.append(L.count(L[i]))
if (max(y))==1:
    print("moda to wszystkie wartości")
else:
    z= y.index(max(y))
    print("moda")
    print(L[z])

Z = sorted(L)

print("Liczby które sie powtarzają: ")
for i in range(len(L)-1):
    if Z[i]==Z[i+1]:
        print(Z[i])
    else:
        k += 1;
        if k==(len(L)-1):
            print ("Liczby sie nie powtarzają")
time.sleep(1)
end = time.time()
finish = end - start - 1
print('Czas wykonywania programu w sekundach(więcej = gorzej):')
print(finish)