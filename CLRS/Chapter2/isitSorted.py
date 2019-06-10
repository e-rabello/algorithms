def notSorted(A):
    
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            return False
        
    return True
