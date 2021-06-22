#Given an array A of N integers. A subarray is a contiguous sequence of integers
#  in the array. A special subarray is a subarray that contains only unique 
# elements in it (i.e. in which every element occurs exactly once). A score 
# is assigned to every subarray which is equal to the length of that subarray 
# if it is a special subarray, otherwise score is 0. Determine the total sum of scores
#  of every subarray.

def subarraySum(A):
    if len(A) == 0:
        return 0
    sum1 = 0
    ptr = 0
    l = []
    for i in range(len(A)):

        while (ptr < len(A)) and (A[ptr] not in l):
            l.append(A[ptr])
            ptr += 1
            
        n = ptr - i
        sum1 = n*(n+1)//2 +  sum1
        l.remove(A[i])
    return sum1
    



if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(subarraySum(arr))