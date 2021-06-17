# Given two arrays index and nums create a target array
#Initially target array is empty.
#From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#Repeat the previous step until there are no elements to read in nums and index.
def createTargetArray(nums, index):
    length = len(nums)
    # base case
    if len(nums) != len(index):
        print("The two arrays should be of same length")
    #lenght of nums, index arrays will be same
    target = [] 
    for i in range(length):
        # if any value in index array is greater than lenght 
        # then append that in the target array 
        if index[i] >= length:
            target.append(nums[i])
        else:
            target.insert(index[i], nums[i])
    return target

if __name__ == "__main__":
    A = [0,1,2,3,4,6,7]
    B = [0,1,1,2,2,3,5]
    print(createTargetArray(A, B))