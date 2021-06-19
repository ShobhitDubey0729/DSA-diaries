# Suppose an array sorted in ascending order is rotated at some pivot unknown
#  to you beforehand.You are given a target value that is sum of two elements in 
# the array. If found in the array return true, otherwise return false.
# we can do it in O(n) time but try to do it in O(logn) time
def sumSortedRotated(A, k):
    """
        A: input array
        k: sum to be searched 
        output: true or false
    """
    if len(A) == 0:
        print("The array is empty")
    # Take two pointers
    left = 0 # traverses left to right
    right = 0 # traverses right to left 
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            left = (i+1) % len(A)
            right = i
    # now we got the location of the left and right pointer   
    while left != right:
        if A[right]+A[left] == k:
            return True
        elif A[right]+A[left] > k:
            right = (len(A)+right-1) % len(A)
        else:
            left = (left+1) % len(A)
    return False

if __name__ =="__main__":
    arr = [11,15,26,38,9,10]
    sum = 35
    print(sumSortedRotated(arr, sum))
