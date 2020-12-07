import numpy as np
import re
import string

file1 = open("Day7Data.txt", 'r')
Lines = file1.readlines()
file1.close()

def FindColors(lines):
	added = AddGroups(lines)
	added = added.translate(str.maketrans('','',string.punctuation)) #remove punctuation
	words = added.split()

	colors = []
	for i in range(len(words)):
		if words[i]=="bags" or words[i]=="bag":
			colors.append(words[i-2]+" "+words[i-1])

	colors=list(set(colors))

	return colors

def AddGroups(ppl):
	added = ""
	for i in range(len(ppl)):
		added+=ppl[i]
	return added


def EndBags(lines):
	endBags = []
	for i in range(len(lines)):
		ind = lines[i].find("contain")
		postContainLine = lines[i][ind+8:]

		if postContainLine.find("shiny gold") != -1:
			words = lines[i].split()
			endBags.append(words[0]+" "+words[1])

	return endBags

def BackProp(lines, bags):
	prevBags = []

	for i in range(len(lines)):
		ind = lines[i].find("contain")
		postContainLine = lines[i][ind+8:]

		for j in range(len(bags)):
			if postContainLine.find(bags[j]) != -1:

				words = lines[i].split()
				prevBags.append(words[0]+" "+words[1])

	prevBags=list(set(prevBags))
	return prevBags


def ForwardProp(lines, bags):
	nextBags = []
	multiplier = []

	for i in range(len(lines)):
		words = lines[i].split()
		ithBag = words[0]+" "+words[1]

		for j in range(len(bags)):
			if ithBag==bags[j]:
				
				#numbInds = [i for i, c in enumerate(lines[i]) if c.isdigit()]
				for k in range(len(words)):
					if words[k].isdigit():
						mult = int(words[k])
						nextBags.append([words[k+1]+" "+words[k+2]]*mult)
						#multiplier.append(k)

	flatten = lambda t: [item for sublist in t for item in sublist]

	return flatten(nextBags)




#colors = FindColors(Lines)
"""
workingBags = []

endBags = EndBags(Lines)


prevBags = endBags
newBags = BackProp(Lines,endBags)

while set(prevBags) != set(newBags):
	workingBags = list(set(prevBags)|set(newBags)|set(workingBags))
	prevBags = newBags
	newBags = BackProp(Lines,newBags)


print(len(workingBags))
"""
totBags = 0
prevBags = ForwardProp(Lines, ['shiny gold'])
nextBags = ForwardProp(Lines, prevBags)
totBags +=len(prevBags)+len(nextBags)

while set(prevBags) != set(nextBags):
	prevBags = nextBags
	nextBags = ForwardProp(Lines, prevBags)
	totBags += len(nextBags)

print(totBags)