import numpy as np

nums = np.genfromtxt("Day9Data.txt").astype(int)
consider = 25


for i in range(consider, len(nums)):
	prev25 = nums[i-consider:i]
	iworks = False

	for j in prev25:
		for k in prev25:
			if j+k==nums[i]:

				iworks = True

	if iworks == False:
		print(i, nums[i])



for i in range(len(nums)):
	for j in range(len(nums)):
		if np.sum(nums[i:j+1]).astype(int)==15690279:
			smallest = np.min(nums[i:j+1])
			largest = np.max(nums[i:j+1])
			print(smallest+largest, i, j)

