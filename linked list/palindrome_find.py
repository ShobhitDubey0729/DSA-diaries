# find if the list is palindrome or not
class node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None
    # class attributes  
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
    
    


def reverse(head):
    prev_of_slow = None
    curr = head
    while curr is not None:
        temp = curr.next 
        curr.next = prev_of_slow
        prev_of_slow = curr
        curr = temp
    head = prev_of_slow
    return head

# using stack(simplest method) //O(n)time and space
def isPalindrome(head):
    ptr = head
    stack = []
    # iterate through list and push in stack
    while ptr is not None:
        stack.append(ptr.data)
        ptr = ptr.next
    #print(stack)

    # now iterate list and stack to compare
    # take a checker which checks after every comparison
    ispalin = True
    while head is not None:
        x = stack.pop()
        if x == head.data:
            ispalin = True

        else: # break the loop if you encounter different elements
            ispalin = False
            break
        head = head.next
    return ispalin




def findPalindrome(llist):
    # use slow and fast pointer to reach mid. we need to take care
    # of the odd case nicely. for that use one extra space to store 
    # middile ele in odd case.
    slow_ptr = llist.head
    fast_ptr = llist.head
    prev_of_slow = llist.head
    if (llist.head != None and llist.head.next != None):
        while fast_ptr != None and fast_ptr.next != None:
            fast_ptr = fast_ptr.next.next
            prev_of_slow = slow_ptr
            slow_ptr = slow_ptr.next
        # if odd elemetns then fast will not be none, fast.next will be none
        mid = None
        if fast_ptr != None:
            mid = slow_ptr
            slow_ptr = slow_ptr.next
        prev_of_slow.next = None
        second_half = slow_ptr
        
        # now reverse the second half and compare
        head2 = reverse(second_half)
        result = compare(llist.head, head2)
    return result




# function to compare the lists
def compare(head1, head2):
    
    while head1 != None and head2 != None:
        if head1.data == head2.data:
            head1 = head1.next
            head2 = head2.next
        else:
            return 'false'
    if head1 is None and head2 is None:
        return 'True'
    
    else:
        return 'false'

# driver code
if __name__=='__main__':
    ll = linkedlist()
    ll.head = node('T')
    ll.push('E')
    ll.push('N')
    ll.push('E')
    ll.push('T')
    print(ll.display())
    print(findPalindrome(ll))