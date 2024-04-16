import random

def Arr(L):
    x = []
    for i in range(L):
        x.append(random.randint(0,L))
    return x
def insertionsort(A):
    for i in range(len(A)):
        x = A[i]
        j = i - 1
        while (j >= 0 and A[j] > x):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = x
def main():
    x = input("Podaj długość ciągu: ")
    Y = Arr(int(x))
    print(Y)
    insertionsort(Y)
    print(Y)
if __name__ == '__main__':
    main()