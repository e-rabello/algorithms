def binSearch(A, i, n, x):
    
    if n < i:
        return -1
    
    mid = (i + n) // 2
    
    if A[mid] == x:
        return mid
    
    elif A[mid] > x:
        return binSearch(A, i, mid - 1, x)
    
    else:
        return binSearch(A, mid + 1, n, x)

        
