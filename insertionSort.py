import random
import time
import numpy as np

def insertSort(nums):
	"""
	Find the maximum number from an array of numbers
	@param Array of numbers
	@return The maximum number
	"""
	start_time = time.time()
	sortSize = len(nums)

	if not isinstance([],list):
		raise Exception('argument is not an array')
	if len(nums) == 1:
		return nums[0]

	result = []
	for curLoop in range(len(nums)):
		curMax = min(nums)
		nums.remove(curMax)
		result.append(curMax)

	#print "InsertSort of %s numbers takes %s seconds" % (sortSize,time.time()-start_time)
	#print result
	#print "Sort finished!"

	return result


def linkedListSort(nums):
	return

if __name__ == "__main__":

	MIN_NUM = 0
	MAX_NUM = 100
	TEST_SIZE = 10000

	testArray = np.random.randint(MIN_NUM, MAX_NUM, TEST_SIZE).tolist()
	testArray.sort()
	#insertSort(testArray)



