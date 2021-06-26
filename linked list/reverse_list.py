# given a linked list; reverse it
class node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def display(self):
        runner = self.head
        if self.head == None:
            print("given list is empty")
        while runner is not None:
            print(runner.data)
            runner = runner.next
    
    def push(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

def reverse(llist):
    prev = None
    curr = llist.head
    while curr is not None:
        temp = curr.next 
        curr.next = prev
        prev = curr
        curr = temp
    llist.head = prev
    

# driver code
if __name__=="__main__":
    ll = linkedlist()
    ll.head = node(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    print(ll.display())
    reverse(ll)
    print(ll.display())

    
