# Given an array nums of n integers where n > 1,  return an array output 
# such that output[i] is equal to the product of all the elements of nums
#  except nums[i].
def productLRSubarray(A):
    n = len(A)
    out = [0]*n
    out[0] = 1
    # left to right and keep track of left product
    for i in range(1,n):
        out[i] = out[i-1]* A[i-1]
    
    # iterate right to left and modify output
    r = 1
    for i in range(n-1, -1, -1):
        out[i] = out[i]*r
        r = r*A[i]
    return out

if __name__=="__main__":
    arr = [1,1,2,2]
    print(productLRSubarray(arr))
    