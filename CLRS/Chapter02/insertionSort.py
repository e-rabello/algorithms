def insertionSort(A):

    for j in range(1, len(A)):
        key = A[j]
        i = j - 1 

        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1
            
        A[i + 1] = key
            


def insertionSortDec(A):

    for j in range(1, len(A)):
        key = A[j]
        i = j - 1 

        while i >= 0 and key > A[i]:
            A[i + 1] = A[i]
            i = i - 1
            
        A[i + 1] = key
            

    
def insertionSortRec(A, n):
# InsertionSort designed by induction(weak)
    if n > 0:
        
        insertionSortRec(A, n - 1)

        key = A[n]
        i = n - 1
        
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key

