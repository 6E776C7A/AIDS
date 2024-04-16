import random
import time

def pomiarmerge(I,L):
    arr = []
    k = 0
    s = 0
    long = -100
    short = 100
    for i in range(I):
        for i in range(L):
            arr.append(random.randint(0, L))
        start = time.time()
        mergesort(arr, 0, len(arr) - 1)
        end = time.time()
        finish = end - start
        k += 1
        s += finish
        if finish >= long:
            long = finish
        if finish <= short:
            short = finish
    sredni = s / k
    print("Mergesort - Sredni czas to %s sekund" % sredni)
    print("Mergesort - Najkrótszy czas wykonwyania to %s  sekund" % short)
    print("Mergesort - Najdłuższy czas wykonwyania to %s sekund" % long)
def pomiarinter(I,L):
    arr = []
    k = 0
    s = 0
    long = -100
    short = 100
    for i in range(I):
        for i in range(L):
            arr.append(random.randint(0, L))
        start = time.time()
        insertionsort(arr)
        end = time.time()
        finish = end - start
        k += 1
        s += finish
        if finish >= long:
            long = finish
        if finish <= short:
            short = finish
    sredni = s/k
    print("Intersort - Sredni czas to %s sekund" % sredni)
    print("Intersort - Najkrótszy czas wykonwyania to %s  sekund" % short)
    print("Intersort - Najdłuższy czas wykonwyania to %s sekund" % long)
def insertionsort(A):
    for i in range(len(A)):
        x = A[i]
        j = i - 1
        while (j >= 0 and A[j] > x):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = x
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
   pomiarinter(100, 1000)
   pomiarmerge(100, 1000)

if __name__ == '__main__':
    main()