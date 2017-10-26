def insertRec(A, n):
# InsertionSort designed by weak induction 
    
    # Base case, one element the array is already sorted
    if n == 1:
        return

    else:
        # By induction we know how to sort the array A[n - 1]
        insertRec(A, n - 1)

        key = A[n - 1]
        i = n - 1 - 1
        
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
            
        A[i + 1] = key

        return
        

def selectionRec(A, n):
# SelectionSort designed by weak induction 
    
    # Base case, one element the array is already sorted
    if n == 1:
        return

    else:

        index = n - 1
        i = n - 2
        
        while i >= 0:
            if A[i] > A[index]:
                index = i
            i = i - 1

        A[index], A[n - 1] = A[n - 1], A[index]
        
        # By induction, we know how to find the max element in the array A[n - 1]
        selectionRec(A, n - 1)


def bubbleRec(A, n):
# BubbleSort designed by weak induction 
    
    # Base case, one element the array is already sorted
    if n == 1:
        return

    else:
        
        i = 0
        
        while i < n - 1:
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
            i = i + 1
        
        # By induction, we know how to find the max element in the array A[n - 1]
        bubbleRec(A, n - 1)


def mergeSort(A, p, q):
# MergeSort designed by strong induction(Divide-and-Conquer)
# To be finished
    if p < q:

        # Divide
        mid = (p + q) // 2

        # By inductive hypothesis, we know how to sort the array A[p:mid]
        mergeSort(A, p, mid)
        # Also by inductive hypothesis, we know how to sort the array A[mid:q]
        mergeSort(A, mid + 1, q)
        
        # Conquer
        merge(A, p, q)
        

def merge(A, p, q):
# Merge
# To be finished
    size = q - p
    

    

#def heapSort(A):
# HeapSort designed by strong induction(Divide-and-Conquer)
# To be implemented

    
#def quickSort(A):
# QuickSort designed by strong induction(Divide-and-Conquer)
# To be implemented
    


