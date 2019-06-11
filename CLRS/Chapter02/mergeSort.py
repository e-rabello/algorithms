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

def isitSorted(A):
# Check if a sequence is sorted
    
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            return False
        
    return True
