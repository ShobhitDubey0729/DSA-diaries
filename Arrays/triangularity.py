def triangleFind(n,A):
    for i in range(len(A)):
        temp1 = A[i]
        temp1 = temp1-(i+1)
        temp2 = A[temp1]
        temp2 = temp2-(i+1)
        if A[temp2]==(i+1):
            return 'YES'
    return 'NO'

A = [4,4,4,2,1]
print(triangleFind(5,A))