def reverse(list, start, stop):
	"""
	start: starting index of the list
	stop: last index of the list
	returns: reversed list
	"""
	# base case
	if (start > stop): 
		print("invalid list")
	else:
		while(start < stop):
			list[start], list[stop] = list[stop], list[start]
			start +=1
			stop -=1
	return list

""" recursive aprroach to solve the same problem"""
def reverse_recursive(list, start, stop):
	if start > stop:
		print("invalid list given")
	else:
		if start < stop:
			list[start], list[stop] = list[stop], list[start]
			reverse_recursive(list, start+1, stop-1)
	return list

if __name__ =='__main__':
	list = [1,2,34,5,6,90,6]
	#reverse(list, 0, len(list)-1)
	#print(reverse_list)
	reversed_list = reverse_recursive(list, 0, len(list)-1)
	print(reversed_list)
