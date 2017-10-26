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
