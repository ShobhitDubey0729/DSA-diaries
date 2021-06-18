# Given an integer array, you need to find one continuous subarray that
# if you only sort this subarray in ascending order, then the whole array
# will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length.
def shortestSubArray(A):
    if len(A) == 0:
        print("The size of the array is zero")

    start = len(A)
    end = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                start = min(start, i)
                end = max(end, j)
    # if array is already sorted then 
    if end-1 < 0:
        return 0
    return [end-start+1]

# But the above algorithm takes O(n*n) time complexity in worst case
# now we will try to do it in O(nlogn) time

def usingSort(A):
    start = len(A)
    end =0
    # copy the given array and sort
    temp = A[:]
    temp.sort()
    for i in range(len(A)):
        if A[i] != temp[i]:
            start = min(start, i)
            end = max(end, i)
    # array is already sorted
    if end - 1 < 0:
        return 0
    return [end-start+1]




if __name__ == "__main__":
    A = [2, 6, 4, 8, 10, 9, 15]
    #print(shortestSubArray(A))
    print(usingSort(A))
    