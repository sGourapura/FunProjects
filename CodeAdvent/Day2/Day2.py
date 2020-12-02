import numpy as np
import re

file1 = open("Day2Data.txt", 'r')
Lines = file1.readlines()
file1.close() 



def Parse(L):
	# Find first number
	dashLoc = Lines[L].find("-")
	firstNList = []
	for i in range(dashLoc):
		firstNList.append(Lines[L][i])
	firstn = ''
	firstN = int(firstn.join(firstNList))

	# Find second number
	spaceLoc = Lines[L].find(" ")
	secondNList = []
	for i in range(dashLoc+1, spaceLoc):
		secondNList.append(Lines[L][i])
	secondn = ''
	secondN = int(secondn.join(secondNList))

	# Find letter
	letter = Lines[L][spaceLoc+1]

	# Find code
	codeList = []
	for i in range(spaceLoc+3, len(Lines[L])-1):
		codeList.append(Lines[L][i])
	code = ''
	code = code.join(codeList)

	return firstN, secondN, letter, code

validCount = 0

for l in range(len(Lines)):

	firstN, secondN, letter, code = Parse(l)

	matches = re.finditer(letter, code)
	numMatches = len([match.start() for match in matches])
	
	if firstN <= numMatches and numMatches <= secondN:
		validCount += 1
	#else:
		#print(firstN,numMatches, secondN)

print("part 1:", validCount)



validCount = 0
for l in range(len(Lines)): #len(Lines)

	firstN, secondN, letter, code = Parse(l)

	firstL = code[firstN]
	secondL = code[secondN]
	
	a =  firstL == letter 
	b =  secondL == letter
	if (a and not b) or (not a and b):
		validCount += 1
		print(l, [firstN, secondN], letter, firstL, secondL, "here")
	else:
		print(l, [firstN, secondN], letter, firstL, secondL)

print("part 2:", validCount)