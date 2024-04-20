import time
def Hanoirec(n,sour,dest,buff):
    if n == 1:
        print("Move disk from {} to {}".format(sour,dest))
        return 1
    moves = 0
    moves += Hanoirec(n-1,sour,buff,dest)
    print("Move disk from {} to {}".format(sour,dest))
    moves += 1
    moves += Hanoirec(n-1,buff,dest,sour)
    return moves

def Hanoiite(n, sour, dest, buff):
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
    n = int(input("How many disks do you want to: "))

    sourrec = 'sour'
    destrec = 'dest'
    buffrec = 'buff'

    sourite = []
    destite = []
    buffite = []

    for i in range(n):
        sourite.append(i + 1)
    sourite.sort(reverse=True)

    startrec = time.time()
    print("Number of moves: ",Hanoirec(n,sourrec,destrec,buffrec))
    time.sleep(1)
    endrec = time.time()
    finishrec = endrec - startrec

    print("Time elapsed for recursive algorithm: ", finishrec-1, "seconds")

    startite = time.time()
    Hanoiite(n, sourite, destite, buffite)
    time.sleep(1)
    endite = time.time()
    finishite = endite - startite

    print("Time elapsed for iteration algorithm: ", finishite-1, "seconds")

if __name__ == '__main__':
    main()