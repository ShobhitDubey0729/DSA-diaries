# given an array of length n and each element of the array ranges from 1 to 
# n-2. find the two repeating elements 
def findRepeating(A):
    n = len(A)
    B = [0]*(n-1)
    for i in range(n):
        B[A[i]] += 1

    for j in range(n-1):
        if B[j] == 2:
            print(j, end=" ")  

# can find best xor based solution. try it
def xorFind(A):
    n = len(A)
    x=0
    y=0
    xor=A[0]
    for i in range(1,n): #This gives value X
        xor^=A[i]
    for i in range(1,n-1):# This gives value Y
        xor^=i
    #Now XOR contains the X XOR Y
    #get the right most bit number
    set_no=(xor) & ~(xor-1)

    #divide the elements into 2 groups based on the right most set bit
    for i in range(n):
        if A[i] & set_no: #we are calculating for set bit for array 
            x^=A[i]
        else:
            y^=A[i]
    for i in range(1,n-1): #we are calculating for set bit for numbers from 1 to m 
        if i & set_no:
            x^=i
        else:
            y^=i
    return x,y
    

if __name__=="__main__":
    A = [1,2,2,3,3,4]
    print(xorFind(A))