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

