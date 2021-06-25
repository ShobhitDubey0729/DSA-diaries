# implementaion of all the methods of linked list
class Node:
    def __init__(self, data):
        self.data =data 
        self.next = None
class linkedList:
    def __init__(self):
        self.head= None

    # now to print the list 
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    # now to insert the node 
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # insert at end. for this we need to traverse the list
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
    
    # insert at a particular position
    def insertAtPosition(self, prev_node, data):
        # check for given prev node
        if prev_node is None:
            print("given pre node does not exist")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    # deletion using data given. 
    # In python garbage is already deleted 
    def deleteNode(self, data):
        if self.head == None:
            print("list is empty")
        # check if head contains the data
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            temp.next = None 
        curr = self.head
        while curr.next != None:
            if curr.next.data == data:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = None
                return 
            curr = curr.next
        print("Given data not found in list")

     # search a particular data   
    def search(self, data):
        if self.head == None:
            print("list is empty")
            return
        curr = self.head
        while curr != None:
            if curr.data == data:
                print("Data found is list")
                return
            curr = curr.next
        print("Data not found in list")

    # counter to know the total length of the list
    def countNodes(self):
        count = 0
        if self.head == None:
            print("list is empty")
            return
        curr = self.head
        while curr != None:
            count += 1
            curr = curr.next
        return count

    # we can insert and delete the nodes by position 
    # in that case we need to find the node just pevious to given position.
    # maintain a counter with while loop to reach there.
            
# driver code
if __name__=="__main__":
    llist = linkedList()
    a = Node(1)
    llist.head = a
    print(llist.printlist())
    llist.insertAtBegin(2)
    llist.insertAtEnd(3)
    llist.insertAtPosition(llist.head.next,4)
    print(llist.printlist()) 
    print(llist.search(4))
    print(llist.deleteNode(2))
    print(llist.search(4)) 
    print(llist.printlist())
    print(llist.countNodes())

