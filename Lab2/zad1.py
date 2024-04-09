L = ''
for i in range(500,3000):
    if (i % 7 == 0) and (i % 5 != 0):
      L += str(i)
print(L.count('21'))
print(L.replace('21','XX'))
