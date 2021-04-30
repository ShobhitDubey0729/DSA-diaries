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

def merge_sorted_list(list1, list2):
	list3 = []

	#if list1 or list2 is empty then print the only one list given
	if list1.head is None:
		printlist(list2)
	elif list2.head is None:
		printlist(list1)
	
	# if both lists are given 
	ptr1 = list1.head
	ptr2 = list2.head
	while ptr1 is not None and ptr2 is not None:
		if ptr1.data == ptr2.data:
			list3.append(ptr1.data)
			list3.append(ptr2.data)
			ptr1 = ptr1.next
			ptr2 = ptr2.next
		elif ptr1.data > ptr2.data:
			
			list3.append(ptr2.data)
			ptr2 = ptr2.next
		elif ptr1.data < ptr2.data:
			list3.append(ptr1.data)
			ptr1 = ptr1.next
		
	#include the leftover when the lenths of both lists are not same
	while ptr1 is not None :
		list3.append(ptr1.data)
		ptr1 = ptr1.next
		

	while ptr2 is not None:
		
		list3.append(ptr2.data)
		ptr2 = ptr2.next
		

	return list3



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
	merged = merge_sorted_list(l1, l2)
	printlist(l1)
	print()
	printlist(l2)
	print()
	print(merged)

	


