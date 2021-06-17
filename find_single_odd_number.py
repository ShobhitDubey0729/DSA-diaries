# we are provided with an arry and need to find the sigle most element 
# which occurs odd number of times
# Shobhit Dubey(IISc)
def find_odd(A):
    n = len(A)
    # base case
    if n==0:
        print("The array is empty")
    else:
        for i in range(n):
            count = 0
            for j in range(n):
                if A[i] == A[j]:
                    count +=1
        if count % 2 != 0:
            print(f'{A[i]} is desired element')
        else:
            print(f'{A[i]} is not desired element')
        return -1

# the above algo is of O(n*n) 
# we wnt to do it O(n) time so use hashtable but it will take O(n) space
# so, we want to do it in O(n) time and O(1) sapace, use XOR operator
def xor_odd_find(A):
    n = len(A)
    # base case
    if n==0:
        print("The array is empty")
    ans = 0
    for i in range(n):
        ans = ans^A[i]
    return ans


# main fuction
if __name__ == "__main__":
    A = [1,2,1,2,3,4,2,2,3,4,2]
    print(xor_odd_find(A))