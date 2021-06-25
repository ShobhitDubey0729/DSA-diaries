class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None

    # printing lsit
    def display(self):
        runner =self.head
        while runner is not None:
            print(runner.data, end=" ")
            runner = runner.next

    # count function to get the length of list
    def countlist(self):
        if self.head == None:
            print("list is empty")
            return

        count = 0
        runner = self.head
        while runner is not None:
            runner = runner.next
            count += 1
        return count
    
    # functio to insert or push in list 
    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        
        new_node.next = self.head
        self.head = new_node

    # function for finding the kth node from end
    def kthFromEnd(self,k):
        #length = self.countlist()
        tp1 = self.head
        tp2 = self.head
        i = 1
        while i < k:
            tp2 = tp2.next
            i += 1
        while tp2.next is not None:
            tp1 = tp1.next
            tp2 = tp2.next
        print(tp1.data)

if __name__ =="__main__":
    llist = linkedlist()
    a = Node(1)
    llist.head = a
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    print(llist.countlist())
    print(llist.display())
    print(llist.kthFromEnd(2))
    

        
