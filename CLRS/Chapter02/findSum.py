#import pdb
#pdb.set_trace()

def mergeSort(A, p, q):
# MergeSort designed by strong induction(Divide-and-Conquer)
    if p < q:

        # Divide
        mid = (p + q) // 2

        # Conquer
        # By inductive hypothesis, we know how to sort the array A[p:mid]
        mergeSort(A, p, mid)
        # Also by inductive hypothesis, we know how to sort the array A[mid+1:q]
        mergeSort(A, mid + 1, q)
        # Combine
        merge(A, p, mid, q)


def merge(A, p, m, q):
# Merge
# Sort two arrays by the interleaving paradigm

    L = A[p:m+1]
    R = A[m+1:q+1]
            
    i = 0
    j = 0
    k = p
    
    # Interleaving paradigm
    # traverse L(Left) and R(Right) from index 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
            k = k + 1
        else:
            A[k] = R[j]
            j = j + 1
            k = k + 1
    # if R is already finished, copy all elements from L back to A
    while i < len(L):
        A[k] = L[i]
        i = i + 1
        k = k + 1
    # if L is already finished, copy all elements from R back to A
    while j < len(R):
        A[k] = R[j]
        j = j + 1
        k = k + 1
        

def findSum(A, x):
#Determines if exists both i and j such that A[i] + A[j] = x

    #Sorts the array
    mergeSort(A, 0, len(A) - 1)

    #Merge modified
    i = 0
    j = len(A) - 1
        
    # Interleaving paradigm
    # traverse the array using two "pointers" i and j
    # i starting from index 0(1st index) and j starting from index len(A) - 1
    # Because A is sorted, we can say that i always points to the minimum element of A and j points to the maximum element of A
    while i < j:

        if A[i] + A[j] == x:
            return i, j

        elif A[i] + A[j] > x:
            j = j - 1
            
        else:
            i = i + 1
            
    return -1, -1
            
def isitSorted(A):
# Check if a sequence is sorted
    
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            return False
        
    return True


    
