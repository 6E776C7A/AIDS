import time

def podaj_slowo():
    slowo = input("Wpisz jakieś słowo: ")
    while True:
        z = slowo.find(' ')
        if z == -1:
            print(slowo, "Jest słowem :)")
            slowo_lower = slowo.lower()
            return slowo_lower
        else:
            print(slowo, "Nie jest słowem :(")
            slowo = input("Podaj jeszcze raz jakieś słowo: ")

def spj(slowo_lower):
    with open('SJP.txt', 'r') as spj:
        text = spj.read()
    while True:
        if slowo_lower not in text:
            print(slowo_lower, "Jest słowem według pwn :)")
            break
        else:
            print(slowo_lower, "Nie jest słowem według pwn :(")
            break
def main():
    start = time.time()
    slowo = podaj_slowo()
    spj(slowo)
    end = time.time()
    finish = end - start
    print("operaja zajeła (s) : ")
    print(finish)

if __name__ == "__main__":
    main()