# There are N positive integers A1, A2, ..., AN. In one operation, shyam can
#  select any number of the array and replace it with any smaller number. 
# He can perform this operation any number of times. Also, he may not apply 
# this to every number in the array. After he is done through applying some 
# operations, the array becomes B1, B2, ..., Bn, where 1 ≤ Bi ≤ Ai for 
# every 1 ≤ i ≤ N. A beautiful number is the minimum number that is not 
# present in this modified array. Determine the maximum possible beautiful number.
def findMaxB(A):
    A.sort()
    ptr = 1
    for i in A:
        if i >= ptr:
            ptr += 1
    return (ptr)

        

        

if __name__=="__main__":
    arr = [4,4,3,4]
    print(findMaxB(arr))