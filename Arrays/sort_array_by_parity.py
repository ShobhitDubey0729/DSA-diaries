# Given an array sort it such that odd elements come after even elements
# Shobhit Dueby(IISc)
def sort_by_parity(A):
    #base case
    if len(A) == 0:
        print("The length of array is zero")
    # Take two pointers one at starting index and one at the end
    ptr1 = 0 
    ptr2 = len(A) - 1
    while ptr1 <= ptr2:
        if A[ptr1]%2 != 0:
            # swap only if the element at ptr1 is odd otherwise increament it
            A[ptr1], A[ptr2] = A[ptr2], A[ptr1]
            ptr2 -= 1
            # decreament ptr2 after every swap
        else:
            ptr1 += 1
    return A

if __name__ == "__main__":
    A = [1,5,2,6,8,3,9,0]
    print(sort_by_parity(A))