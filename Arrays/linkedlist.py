# linkedlist implementation in python 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        

def traversal(list):
    temp = list.head
    if temp == None:
        print("the list is empty")
    else:
        while(temp != None):
            print(temp.data)
            temp = temp.next

def insert_at_beggining(list, data):
    # create a new node first then link to begging
    node = Node(data)
    node.next = list.head
    list.head = node

def insert_at_last(list, data):
    node = Node(data)
    # go to the last node by taking the pointer
    ptr = list.head
    while(ptr.next != None):
        ptr = ptr.next
    ptr.next = node

def insert_in_mid(list, data, k): # k is the node after which we want to insert
    node = Node(data)
    node.next = k.next
    k.next = node

def delete(list, k): # kth node to be delted 
    # there are three cases
    if k == list.head:
        list.head = list.head.next
    elif k.next == None:
        del k
    else:
        temp = list.head
        while(temp.next != k):
            temp = temp.next
        temp.next = k.next
        del k

if __name__== '__main__':
    l = linkedlist(5)
    traversal(l)
    insert_at_beggining(l, 8)
    insert_at_last(l, 4)
    insert_in_mid(l, 2, l.head.next)
    traversal(l)