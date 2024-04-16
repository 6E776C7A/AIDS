import random

def Arr(L):
    x = []
    for i in range(L):
        x.append(random.randint(0,L))
    return x

def merge(arr,a,c,b):
    n1 = c - a + 1
    n2 = b - c

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0,n1):
        L[i] = arr[a+i]
    for i in range(0,n2):
        R[i] = arr[c + 1 + i]
    i = 0
    j = 0
    k = a

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr,a,b):
    if a < b:
        c = (a+b)//2
        mergesort(arr,a,c)
        mergesort(arr,c+1,b)
        merge(arr,a,c,b)

def main():
    x = input("Podaj długość ciągu: ")
    Y = Arr(int(x))
    print(Y)
    mergesort(Y,0,len(Y)-1)
    print(Y)

if __name__ == '__main__':
    main()