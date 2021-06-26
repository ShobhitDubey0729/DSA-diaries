# Given a linked list, determine if it has a cycle in it.
# also famous as fast and slow pointer technique 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.head = None
    
    def display(self):
        runner = self.head
        while runner is not None:
            print(runner.data)
            runner = runner.next

    def push(self, data):
        if self.head is None:
            print("list is empty")
            return

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# function for detecting cycle in the given list   
def detectCycle(llist):
    slow = llist.head
    fast = llist.head.next
    while (slow and fast and fast.next) != None:
        # if fast is head.next then first check then apply next otherwise
        # if fast is intialised as head then first do next then check.
        if slow == fast:
            print("Cycle found in the given list")
            return
        slow = slow.next
        fast = fast.next.next
    print("Cycle not present in given list")

# driver code
if __name__=="__main__":
    
    ll = linkedlist()
    ll.head = Node(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    print(ll.display())
    print(detectCycle(ll))
    ll.head.next.next.next.next.next = ll.head.next.next
    print(detectCycle(ll))
    '''
    # we can give custom input
    ll = linkedlist()
    print("enter the list length")
    n = int(input())
    for i in range(n):
        ll.push(int(input()))
    print(ll.display())
    '''