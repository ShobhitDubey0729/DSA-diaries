# This program counts how many numbers are smalller than the each element given
# in the array and outputs an array consisting of counts at the respective
# element index
# Shobhit Dubey(IISc)

def count_smaller(arr):
    """
    arr: input is list[int] 
    output: a list[int] 
    """
    # base case
    if len(arr) == 0:
        print("There is no element in the array")
    # first sort the given array
    #arr = arr.sort()
    # dont use .sort() method as it returns nothing and can be operated on lists only
    # on the other hand sorted() return iterable list and can be operated on list, dict
    # or string. also, it doesn't change the original input 
    # iterate over to make a hashtable
    count = {}
    for k, v in enumerate(sorted(arr)):
        # check if value is not in hashtable then only add it
        # so it will remove duplicates
        if v not in count:
            count[v] = k
    return [count[v] for v in arr]
    
# main function
if __name__ == "__main__":
    A = [1,2,2,3,5]
    #A = []
    print(count_smaller(A))