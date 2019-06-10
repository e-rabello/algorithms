def linearSearch(A, key):

    for i in range(0, len(A)):

        if key == A[i]:
            return i
        

    return -1
