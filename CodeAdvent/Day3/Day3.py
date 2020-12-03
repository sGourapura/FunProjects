import numpy as np
import re

file1 = open("Day3Data.txt", 'r')
Lines = file1.readlines()
file1.close() 
"""
for i in rage(len(Lines)):
	Lines 
"""

# Digitize data
data = np.zeros((len(Lines), len(Lines[0]))).astype(int)

for i in range(len(Lines)):
	ts = re.finditer('#', Lines[i])
	tArr = [t.start() for t in ts]
	for j in range(len(tArr)):
		data[i, tArr[j]] = 1

def numTrees(xStep, yStep):
	encounters = 0
	xPos = 0
	for i in range(int(len(Lines)/yStep)): #len(Lines)
		encounters += data[i*yStep, xPos]

		xPos += xStep

		if xPos >= 31:
			xPos -= 31
	return encounters

xSteps = [1, 3, 5, 7, 1]
ySteps = [1, 1, 1, 1, 2]
mult = 1
for i in range(5):
	mult *= numTrees(xSteps[i], ySteps[i])

print(mult)