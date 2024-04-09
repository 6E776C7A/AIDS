x = []
y = []
#odczyt pliku i zapisanie pliku bez pustych wartości val w liście i zmiana dużych liter na małe
with open('zadanie2.csv', 'r') as my_file:
    for line in my_file:
        if str(line.split(',')[1]) != '\n':
            line_lower = line.lower()
            x.append(line_lower)
#tworzenie krotki dwuwymiarowej z pierwszą wartoscia int a drugą string
for i in x:
    text = str(i.split(',')[1])
    try:
        id = int(i.split(',')[0])
    except ValueError:
        pass
    else:
        y.append([id, text])
#sortowanie krotki żeby łatwo naprawić ineksy
sorted_y = sorted(y, key=lambda x: x[0])
#naprawienie indeksów/zrobienie ich od nowa
j=1
for i in range(len(y)):
    sorted_y[i][0] = j
    j+=1

#znaki ASCII usuwanie wyrazu (źle zrobione)
i=0
while i < len(sorted_y):
    if abs(ord(sorted_y[i][1][0]) - ord(sorted_y[i][1][1])) == 1:
        print("id:", sorted_y[i][0], "val:", sorted_y[i][1])
        sorted_y.pop(i)
        i -= 1
    i += 1