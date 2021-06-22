# find leaders in given array

def findLeaders(A):
    if len(A) == 0:
        print("The given array is empty")
    n = len(A)
    max_sofar = 0
    leaders = []
    for i in range(len(A)-1, -1, -1):
        # iterate right to left and update max_sofar
        if A[i] > max_sofar:
            leaders.append(A[i])
            max_sofar = A[i]
    return leaders

if __name__ == "__main__":
    arr = [8,4,2,3,1,5,4,2]
    print(findLeaders(arr))