import numpy as np

file1 = open("Day6Data.txt", 'r')
Lines = file1.readlines()
file1.close()

def ParseAns(lines):
	ppl =[[]]
	ind = 0

	for i in range(len(lines)):
		if lines[i] != "\n":
			ppl[ind].append(lines[i].strip("\n"))
		else:
			ind+=1
			ppl.append([])
	return ppl

def AddGroups(ppl):
	added = []
	for i in range(len(ppl)):
		ans = ""
		for j in range(len(ppl[i])):
			ans += ppl[i][j]
		added.append(ans)
	return added

def RemoveDuplicated(ppl):
	unique = []  
	for i in range(len(ppl)):
		unique.append("".join(set(ppl[i])) )

	return unique


"""
parsedAns = ParseAns(Lines)
#print(parsedAns)
addedAns = AddGroups(parsedAns)
#print(addedAns)
strainedAns = RemoveDuplicated(addedAns)
#print(strainedAns)
counts = []
for i in range(len(strainedAns)):
	counts.append(len(strainedAns[i]))

print(np.sum(np.array(counts)))
"""

parsedAns = ParseAns(Lines)
counts = np.zeros(len(parsedAns)).astype(int)

for i in range(len(parsedAns)):

	for j in range(len(parsedAns[i][0])):

		jPasses = True
		for k in range(1, len(parsedAns[i])):
			ind = parsedAns[i][k].find(parsedAns[i][0][j])
			if ind == -1:
				jPasses = False
				break

		if jPasses:
			counts[i] += 1


print(counts)
print(np.sum(np.array(counts)))