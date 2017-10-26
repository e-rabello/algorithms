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
