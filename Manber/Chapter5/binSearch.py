def binSearch(A, x, i, j):
# BinarySearch algorithm designed by induction

    if i == j:
        if A[i] == x:
            return i
        else:
            return -1

    else:
        mid = (i + j) // 2


        if A[mid] >= x:
            return binSearch(A, x, i, mid)
        else:
            return binSearch(A, x, mid + 1, j)
    
 

def binSearchCyclic(A, i, j):
# BinarySearch algorithm in a cyclic array designed by induction

    if i == j:
        return i

    else:
        mid = (i + j) // 2

        if A[mid] < A[j]:
            return binSearchCyclic(A, i, mid)
        else:
            return binSearchCyclic(A, mid + 1, j)



def binSearchCyclicSpecial(A, x, i, j):
# To be implemented

