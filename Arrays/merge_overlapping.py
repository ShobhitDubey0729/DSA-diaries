# Given an array of arr where arr[i] = [start_i, end_i], merge all
#  overlapping arr, and return an array of the non-overlapping arr
#  that cover all the arr in the input
def mergeOverlapping(arr):
    # sort array using arr[i][0] value
    arr.sort(key= lambda x: x[0])
    # initialise the stack
    out = [arr[0]]
        
    for i in range(1, len(arr)):
        #check for a merge
        if arr[i][0] <= out[-1][1]:
            out[-1] = [out[-1][0], max(out[-1][1],arr[i][1])]
        else:
            out.append(arr[i])
            
    return out
        
if __name__=="__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(mergeOverlapping(intervals))