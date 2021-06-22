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
    for i in range(1,length):
        # if any value in index array is greater than lenght 
        # then append that in the target array 
       # if index[i] > length+1:
        #    target.append(nums[i])
        
        target.insert(index[i], nums[i])
    for i in range(1,length):
        if nums[i] != index[i] and index[i] != target[i]:
            print("YES")
    return target

if __name__ == "__main__":
    A = [1,2,3,4,5]
    B = [3,4,5,2,1]
    print(createTargetArray(A, B))