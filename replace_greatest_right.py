# Given an array arr, replace every element in that array with the 
# greatest element among the elements to its right, and replace the
#  last element with -1
# Shobhit Dubey
def replaceRightGreatest(A): # takes an array and returns array
    #base case
    if len(A) == 0:
        print("The length of array is zero")
    max_sofar = -1
    # loop form right to left and update
    for i in range(len(A)-1, -1, -1):
        temp = A[i]
        A[i] = max_sofar
        if max_sofar < temp:
            max_sofar = temp
    return A

if __name__ == "__main__":
    A = [17,18,5,4,6,1]
    print(replaceRightGreatest(A))
        
        
            


            

