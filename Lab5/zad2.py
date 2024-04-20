def Hanoi(n, sour, dest, buff):
    i = 1
    while (sour != [] or buff != []):
        if i % 3 == 1:
            #Possible move disk between sour and dest
            if len(sour)==0:
                sour.append(dest.pop())
                print("Move disk from dest to sour")
            elif len(dest)==0:
                dest.append(sour.pop())
                print("Move disk from sour to dest")
            elif sour[-1] < dest[-1]:
                dest.append(sour.pop())
                print("Move disk from sour to dest")
            else:
                sour.append(dest.pop())
                print("Move disk from dest to sour")
        elif i % 3 == 2:
            #Possible move disk between sour and buff
            if len(sour)==0:
                sour.append(buff.pop())
                print("Move disk from buff to sour")
            elif len(buff)==0:
                buff.append(sour.pop())
                print("Move disk from sour to buff")
            elif sour[-1] < buff[-1]:
                buff.append(sour.pop())
                print("Move disk from sour to buff")
            else:
                sour.append(buff.pop())
                print("Move disk from buff to sour")
        elif i % 3 == 0:
            #Possible move disk between buff and dest
            if len(buff)==0:
                buff.append(dest.pop())
                print("Move disk from dest to buff")
            elif len(dest)==0:
                dest.append(buff.pop())
                print("Move disk from buff to dest")
            elif buff[-1] < dest[-1]:
                dest.append(buff.pop())
                print("Move disk from buff to dest")
            else:
                buff.append(dest.pop())
                print("Move disk from dest to buff")
        i += 1
    print("Number of moves: ", i-1)

def main():
    sour = []
    dest = []
    buff = []
    n = int(input("How many disks do you want to: "))
    for i in range(n):
        sour.append(i+1)
    sour.sort(reverse = True)
    Hanoi(n, sour, dest, buff)

if __name__ == '__main__':
    main()