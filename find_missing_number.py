# given n value and array find the missing value which can be
#  any one integer from 1 to n . only O(n) or lesser time complexity.
# Shobhit Prakash Dubey(Mtech IISc)

A = [1,2,3,4,6,7,8,9,10]
n = 10 

def find_missing(n, Array):
    S = sum(A) # order of O(n)
    sum_of_first_n_nos = n*(n+1)/2 # O(1)
    return [sum_of_first_n_nos-S]

print(find_missing(10, A))

# remember if n is very large then n(n+1) can create numerical overflow problem.
# to avoid this we can use XOR based solution where number of bits don't increase 
# as in case of previous sol n*n
def xor_find(n, array):
    x = 0
    for i in range(1,n+1):
        x = x^i
    y = 0
    for j in range(len(A)):
        y = y^A[j]
    return [x^y]

print(xor_find(10,A))