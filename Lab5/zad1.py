def Hanoi(n,sour,dest,buff):
    if n == 1:
        print("Move disk from {} to {}".format(sour,dest))
        return 1
    moves = 0
    moves += Hanoi(n-1,sour,buff,dest)
    print("Move disk from {} to {}".format(sour,dest))
    moves += 1
    moves += Hanoi(n-1,buff,dest,sour)
    return moves

def main():
    n = int(input("How many disks do you want to: "))
    sour = 'sour'
    dest = 'dest'
    buff = 'buff'
    print("Number of moves: ",Hanoi(n,sour,dest,buff))

if __name__ == '__main__':
    main()