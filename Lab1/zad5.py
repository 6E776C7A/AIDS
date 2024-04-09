import random

def wyslietl_plansza(plansza):
    pustaplansza="""
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
"""
    for i in range(1,10):
        if (plansza[i] == 'O' or plansza[i] == 'X'):
            pustaplansza = pustaplansza.replace(str(i), plansza[i])
        else:
            pustaplansza = pustaplansza.replace(str(i), ' ')
    print(pustaplansza)

def tryb_gry():
    gracz = input('Wybierz tryb gry(gracz czy komputer): ')
    while True:
        if gracz == 'gracz':
            tryb = 'gracz'
            print('Wybrano tryb gry: Gracz vs Gracz')
            return tryb
            break
        elif gracz == 'komputer':
            tryb = 'komputer'
            print('Wybrano tryb gry: Gracz vs Komputer')
            return tryb
            break
        else:
            gracz = input('Niepoprawny wybór. Wybierz tryb gry(gracza czy komputer): ')

def gracz_gracz():
    gracz1 = input("Wybierz twój znak 'X' lub 'O': ")
    while True:
        if gracz1 == 'X':
            gracz2 = 'O'
            print('Gracz 1 wybrał: ' + gracz1 +', Gracz 2 będzie: '+ gracz2)
            return gracz1,gracz2
        elif gracz1 == 'O':
            gracz2 = 'X'
            print('Gracz 1 wybrał: ' + gracz1 +', Gracz 2 będzie: '+ gracz2)
            return gracz1,gracz2
        else:
            gracz1 = input("Niepoprawny wybór. Wybierz twój znak 'X' lub 'O': ")

def gracz_komputer():
    gracz1 = input("Wybierz twój znak 'X' lub 'O': ")
    while True:
        if gracz1 == 'X':
            komputer = 'O'
            print('Gracz 1 wybrał: ' + gracz1 + ', Komputer będzie: ' + komputer)
            return gracz1,komputer
        elif gracz1 == 'O':
            komputer = 'X'
            print('Gracz 1 wybrał: ' + gracz1 + ', Komputer będzie: ' + komputer)
            return gracz1,komputer
        else:
            gracz1 = input("Wybierz poprawnie 'X' lub 'O'")

def sprawdzanie_miejsca(plansza, pozycja):
    return plansza[pozycja] == '#'

def wybur_pozycji(plansza):
    wybur = input("Wybierz pozycje wstawienia znaku od 1 do 9: ")
    while not sprawdzanie_miejsca(plansza, int(wybur)):
        wybur = input("Miejsce jest zajęte.Wybierz pozycje wstawienia znaku od 1 do 9: ")
    return wybur

def postaw_znak(plansza, znak, pozycja):
    plansza[pozycja] = znak
    return plansza

def pozycja_komputer(plansza, wybory_gracza):
    pola = [1,2,3,4,5,6,7,8,9]
    wolne_pola = [];
    for p in pola:
        if p in wybory_gracza:
            continue;
        wolne_pola.append(p);
    wybur = random.choice(wolne_pola)
    return wybur

def sprawdzanie_wygranej(plansza, znak):
    for i in range(3):
        if plansza[1+(i*3)] == plansza[2+(i*3)]== plansza[3+(i*3)] == znak:
            return True
        elif plansza[1+i] == plansza[4+i] == plansza[7+i] == znak:
            return True
        elif plansza[1] == plansza[5] == plansza[9] == znak:
            return True
        elif plansza[3] == plansza[5] == plansza[7] == znak:
            return True
    return False

def main():
    zajete_pola = []
    x = 1
    y = 0
    print('Witam w grze kółko i krzyżyk!')
    plansza = ['#'] * 10
    print('Oto plansza do gry:')
    wyslietl_plansza(plansza)
    while True:
        tryb=tryb_gry()
        if tryb == 'gracz':
            gracze = gracz_gracz()
            while True:
                y += 1;
                pozycja = wybur_pozycji(plansza)
                if x % 2 == 1:
                    znak = gracze[0]
                else:
                    znak = gracze[1]
                postaw_znak(plansza, znak, int(pozycja))
                wyslietl_plansza(plansza)
                x += 1
                if sprawdzanie_wygranej(plansza, znak):
                    print("Koniec gry wygrał: " + znak)
                    break
                if y == 9:
                    print("Koniec gry, wynikiem jest remis!")
                    break
            break
        elif tryb == 'komputer':
            gracze = gracz_komputer()
            x = random.randint(0,1)
            if x == 0:
                print("Zaczyna komputer")
            else:
                print("Zaczyna gracz")
            while True:
                y += 1
                if x % 2 == 1:
                    pozycja = wybur_pozycji(plansza)
                    zajete_pola.append(int(pozycja))
                    znak = gracze[0]
                    postaw_znak(plansza, znak, int(pozycja))
                    wyslietl_plansza(plansza)
                else:
                    pozycja = pozycja_komputer(plansza, zajete_pola)
                    zajete_pola.append(int(pozycja))
                    znak = gracze[1]
                    postaw_znak(plansza, znak, int(pozycja))
                    print("Ruch komputera: ")
                    wyslietl_plansza(plansza)
                x += 1
                if sprawdzanie_wygranej(plansza, znak):
                    print("Wygrał: " + znak)
                    break
                if y == 9:
                    print("Koniec gry, wynikiem jest remis!")
                    break
            break


if __name__ == "__main__":
    main()