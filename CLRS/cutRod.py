def cutRod(p, n):
# Naive recursive solution for the Rod Cutting problem
# p = list of prices
# n = rod length

    if n == 0:
        return 0

    q = 0
    
    for i in range(1, n):
        q = max(q, p[i] + cutRod(p, n - i - 1))

    return q
                   
    

# list of prices
l = [1,5,8,9,10,17,17,20,24,30]

