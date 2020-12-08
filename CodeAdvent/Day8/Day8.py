import numpy as np
#import re
#import string

file1 = open("Day8Data.txt", 'r')
Lines = file1.readlines()
file1.close()

def Parse(lines):
	cmd = []
	val = []
	for i in range(len(lines)):
		cmd.append(lines[i][:3])
		num = lines[i][3:]
		val.append(int(num.strip()))
	return cmd, val


cmd, val = Parse(Lines)
#print(cmd, val)
"""
accu = 0
linesUsed = np.zeros((len(Lines))).astype(int)
lineInd = 0

while linesUsed[lineInd] == 0:
	myCmd, myVal = cmd[lineInd], val[lineInd]
	linesUsed[lineInd] = 1
	#print(lineInd, myCmd, myVal, accu)
	if myCmd =="nop":
		lineInd += 1

	elif myCmd == "acc":
		accu += myVal
		lineInd += 1	

	elif myCmd == "jmp":
		lineInd += myVal

print(accu)
"""

def GenPossibleCmds(cmd):
	allCmd = []

	#nJmp = len([i for i, x in enumerate(cmd) if x == "jmp"])
	#nNop = len([i for i, x in enumerate(cmd) if x == "nop"])
	for i in range(len(cmd)):
		if cmd[i] == "jmp":
			tempCmd = cmd.copy()
			tempCmd[i] = 'nop'
			allCmd.append(tempCmd)
	for i in range(len(cmd)):
		if cmd[i] == "nop":
			tempCmd = cmd.copy()
			tempCmd[i] = 'jmp'
			allCmd.append(tempCmd)
	return allCmd



allcmd = GenPossibleCmds(cmd)


for i in range(len(allcmd)):

	accu = 0
	linesUsed = np.zeros((len(Lines))).astype(int)
	lineInd = 0
	while linesUsed[lineInd] == 0: #or lineInd >= len(Lines)
		myCmd, myVal = allcmd[i][lineInd], val[lineInd]
		linesUsed[lineInd] = 1
		#print(lineInd, myCmd, myVal, accu)
		if myCmd =="nop":
			lineInd += 1

		elif myCmd == "acc":
			accu += myVal
			lineInd += 1	

		elif myCmd == "jmp":
			lineInd += myVal

		if lineInd >= len(Lines):
			print(accu)


