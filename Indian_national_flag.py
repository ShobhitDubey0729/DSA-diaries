# Given an array with n objects colored saffron, white or green, sort them 
# in-place so that objects of the same color are adjacent, with the colors
#  in the order saffron, white and green. Here, we will use the integers 0, 1, and 2 to 
# represent the color saffron, white, and green respectively.
# You are not suppose to use the library's sort function for this problem.

def brutForce(A):
    if len(A) == 0:
        print(" The given array has 0 length")
    # loop over the array three times 
    out = [] # O(n) space
    for i in range(len(A)):
        if A[i] == 0:
            out.append(A[i])

    for i in range(len(A)):
        if A[i] == 1:
            out.append(A[i])

    for i in range(len(A)):
        if A[i] == 2:
            out.append(A[i])
    return out

# now we can use bucket or counting sort for this algorithm. but here we will return 
# number of times the digits 0, 1 and 2 appears as output. if we want to return sorted
# array then we can replace the values in the same array 
def countingColors(A):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(A)):
        if A[i] == 0:
            count1 += 1
        elif A[i] == 1:
            count2 += 1
        else:
            count3 += 1
    out = [] # O(n) space
    out.append(0*count1)
    out.append(1*count2)
    out.append(2*count3)
    return out

# three pointer technique
def bestSolution(A):
    left = 0
    right = len(A)-1
    curr = 0
    while (curr < right):
        if A[curr]==0:
            A[curr], A[left] = A[left], A[curr] 
            left += 1
            curr += 1
        elif A[curr] == 1:
            curr += 1
        elif A[curr] == 2:
            A[curr], A[right] = A[right], A[curr]
            right -= 1
    return A
        
if __name__ == "__main__":
    arr = [0,1,2,0,1,2,0,0,1,1,2,2,1]
    #print(brutForce(arr))
    #print(countingColors(arr))
    print(bestSolution(arr))