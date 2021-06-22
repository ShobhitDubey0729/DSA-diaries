
def compute_lcm(a, b):

   # choose the greater number
   if a > b:
       greater = a
   else:
       greater = b

   while(True):
       if((greater % a == 0) and (greater % b == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
def equalArray(A, x,y,z):

    for i in range(len(A)):
        while A[i] % x == 0:
            A[i] = A[i] // x
        
        while A[i] % y == 0:
            A[i] = A[i] // y

        while A[i] % z == 0:
            A[i] = A[i] // z
        
        
    if min(A) == max(A):
        return "She can"
    else:
        return "She can't"
        
        

if __name__ == "__main__":
    arr = [2, 6, 7]
    print(equalArray(arr, 2,3,2))