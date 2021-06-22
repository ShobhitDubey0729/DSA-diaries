class Node:
	def __init__(self, data):
		self.next = None
		self.data = data

class list:
	def __init__(self,  data):
		new_node = Node(data)
		self.head = new_node

def merge_sorted_list(list1, list2):
	list3 = list(0)
	root = list3
	ptr1 = list1.head
	ptr2 = list2.head
	while ptr1 != None or ptr2 != None:
		if ptr1.data == ptr2.data:
			list3.next = list(ptr1.data)
			list3.next = list(ptr2.data)
			list3 = list3.next
			ptr1 = ptr1.next
			ptr2 = ptr2.next
		elif ptr1.data > ptr2.data:
			list3.next = list(ptr2.data)
			ptr2 = ptr2.next
			list3 = list3.next
		elif ptr1.data < ptr2.data:
			list3.next = list(ptr1.data)
			ptr1 = ptr1.next
			list3 = list3.next
	#include the leftover
	while ptr1 != None:
		list3.next = list(ptr1.data)
		ptr1 = ptr1.next
		list3 = list3.next

	while ptr2 != None:
		list3.next = list(ptr2.data)
		ptr2 = ptr2.next
		list3 = list3.next

	return root.next


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
	merge_sorted_list(l1, l2)

	


