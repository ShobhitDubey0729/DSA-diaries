
def twoSum(nums, target):
	hash_table = dict()
	for i in range(len(nums)):
		temp = target - nums[i]
		if temp in hash_table:
			return (hash_table[temp], i)
		else:
			hash_table[nums[i]] = i
	return hash_table
    

if __name__ == '__main__':
  	List = [1,3,5,2,7,8]
  	twoSum(List, 9)
  
