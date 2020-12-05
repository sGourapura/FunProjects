import numpy as np

file1 = open("Day5Data.txt", 'r')
Lines = file1.readlines()
file1.close()


def findID(line):
	fb = line[:7]
	lr = line[7:]

	FB = fb.replace("B", "1")
	FB = FB.replace("F", "0")

	LR = lr.replace("R", "1")
	LR = LR.replace("L", "0")

	FB = int(FB, 2)
	LR = int(LR, 2)

	return FB*8+ LR


biggest = 0
smallest = 99999
ids = []
for i in range(len(Lines)):
	if biggest < findID(Lines[i]):
		biggest = findID(Lines[i])
	if smallest > findID(Lines[i]):
		smallest = findID(Lines[i])
	ids.append(findID(Lines[i]))

print(biggest, smallest)

#print(ids)

for i in range(smallest, biggest):
	if not(i in ids):
		print(i)
	