""" 
merging two sorted list in python
input: two singly linked list
output: one single list 
"""

class Node:
	def __init__(self, data):
		self.next = None
		self.data = data

class list:
	def __init__(self,  data):
		new_node = Node(data)
		self.head = new_node

# for printing list
def printlist(llist):
	while llist.head is not None:
		print(llist.head.data, end=" ")
		llist.head = llist.head.next

def merge_sorted(head1, head2):

	#if list1 or list2 is empty then print the only one list given
	if head1 is None:
		printlist(head2)
	if head2 is None:
		printlist(head1)

			
	if head1.data > head2.data:
		head2.next = merge_sorted(head1, head2.next)
		return head2
	else:
		head1.next = merge_sorted(head1.next, head2)
		return head1
			



if __name__ =='__main__':
	l1 = list(4)
	a = Node(20)
	b = Node(50)
	c = Node(60)
	l1.head.next = a
	a.next = b
	b.next = c
	l2 = list(4)
	d = Node(25)
	e = Node(50)
	l2.head.next = d
	d.next = e
	merged = merge_sorted(l1.head, l2.head)
	printlist(l1)
	print()
	printlist(l2)
	print()
	print(merged)

	


