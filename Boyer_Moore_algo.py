# To find the majority element in an given array
A = [2,1,3,2,4,2,2,5,2]
n = len(A)
# an element is majority element if it occurs more than n/2 times in the array

def find_majority(n, Array):
    # base case
    if n == 0:
        print("Array is empty")
    count  = 0
    temp = 0
    for i in range(n):
        if count == 0:
            temp = A[i]
            count += 1
        else:
            if temp == A[i]:
                count += 1
            else:
                count -= 1
    count2 = 0

    for j in range(n):
        if temp == A[j]:
            count2 = count2 + 1
        
    if count2 > n/2:
        print(f'{temp} is a majority element')
    else:
        print('There is no majority element')
    return 0

find_majority(n, A)