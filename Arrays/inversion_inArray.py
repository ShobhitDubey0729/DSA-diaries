# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
# global inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
# Return true if and only if the number of global inversions is equal to the number of
#  local inversions.
from typing import Counter


def findInversions(A):
    n =len(A)
    temp = A[:]
    temp = temp.sort()
    count = 0
    for i in range(n):
        if temp[i]^A[i] != 0:
            count += 1
    return count, temp

if __name__=="__main__":
    arr = [2,5,1,7,9]
    print(findInversions(arr))
