# rotate array clockwise or acw m times
# Shohit Dubey(IISc)
def rotate_once_ACW(A):
    # base case
    if len(A) == 0:
        print("The array is empty")
    n = len(A)
    temp = A[n-1]
    for i in range(n-2, -1, -1):
        A[i+1] = A[i]

    A[0] = temp
    return [A]

# now to rotate the Array m times
# the time complexity is O(n*m) so polynomial
def rotate_times(m, A):
    for i in range(m):
        rotate_once_ACW(A)
    return A    

# now to do in linear time and O(1) space
def reverse(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start +=1
        end -=1
    return A

# write a function to rotate m times usign reverse function
def rotate_ACW(A, m):
        # base case
    if len(A) == 0:
        print("The array is empty")
    else:
        n = len(A)
        # first reverse last m elements
        reverse(A, n-m, n-1)
        # then reverse left out elements
        reverse(A, 0, n-m-1)
        # then reverse all elements again to get desired output
        reverse(A, 0, n-1)
    return A
if __name__ == "__main__":
    A = [1,3,4,5,6,6,7]
    #A = [] to check the output in base case
    print(rotate_ACW(A, 3))