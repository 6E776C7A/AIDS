import time

letters = ['a','b','c','d','e','f']

for1 = time.time()
#pętla for zaczerpnięta z c++, iterowanie po liście
for l in letters:
    print(l)

time.sleep(1)
end1 = time.time()
fiish1 = end1-for1 - 1

print('czas wykonywanie pierwszego for: ')
print(fiish1)

for2 = time.time()
#pętla for python, zamienia listę na sekfencje numerów
#pętle żeby zwracały to samo trzeba print(l) zamienić na print(letters[l])
for l in range(len(letters)):
    print(l)

time.sleep(1)
end2 = time.time()
fiish2 = end2-for2 - 1

print('czas wykonywanie drugieego for: ')
print(fiish2)