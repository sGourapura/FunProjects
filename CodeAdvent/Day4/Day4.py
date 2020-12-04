import numpy as np
import re

#file1 = open("testData.txt", 'r')
file1 = open("Day4Data.txt", 'r')
Lines = file1.readlines()
file1.close() 

def ParsePassport(lines):
	pports = [""]
	ind = 0

	for i in range(len(lines)):
		pports[ind] += lines[i]
		if lines[i] == "\n":
			ind+=1
			pports.append("")
	return(pports)


def Parse(passport):
	things = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
	values = []


	for i in range(len(things)):
		dashLoc = passport.find(things[i])

		if dashLoc==-1:
			return 0

		truncPass = passport[dashLoc:]
		spLoc = truncPass.find(" ")
		nlLoc = truncPass.find("\n")
		nlnlLoc = truncPass.find("\n\n")

		if spLoc == -1:
			spLoc = 10000
		if nlLoc == -1:
			nlLoc = 100000
		if nlnlLoc == -1:
			nlnlLoc = 1000000
	
		values.append(truncPass[ 4: min(spLoc, nlLoc, nlnlLoc)])
	


	return values

def cond(values):

	#validChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
	validChars = "0123456789abcdef"
	validNums = "0123456789"
	eyeC = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

	if int(values[0]) < 1920 or int(values[0]) > 2002:
		print("0")
		return 0

	if int(values[1]) < 2010 or int(values[1]) > 2020:
		print("1")
		return 0

	if int(values[2]) < 2020 or int(values[2]) > 2030:
		print("2")
		return 0

	if values[3][-2:]=="cm":
		if int(values[3][:-2]) < 150 or int(values[3][:-2]) > 193:
			print("3")
			return 0
	elif values[3][-2:] =="in":
		if int(values[3][:-2]) < 59 or int(values[3][:-2]) > 76:
			print("4")
			return 0
	else:
		print("5",values[3], values[3][-2:])
		return 0

	if values[4][0]=="#":
		if len(values[4][1:]) != 6:
			print("6")
			return 0
		else:
			for i in range(6):
				if validChars.find(values[4][i+1]) == -1:
					print("7", values[4][i+1])
					return 0
	else:
		return 0

	if values[5] != eyeC[0] and values[5] != eyeC[1] and values[5] != eyeC[2] and values[5] != eyeC[3] and values[5] != eyeC[4] and values[5] != eyeC[5] and values[5] != eyeC[6]:
		print("8")
		return 0

	if len(values[6]) != 9:
		print("9")
		return 0
	else:
		for i in range(9):
			if validNums.find(values[6][i]) == -1:
				print("10")
				return 0

	
	return 1

passports = ParsePassport(Lines)

Sum = 0
for i in range(len(passports)): #len(passports)
	print("loop",i)
	vals = Parse(passports[i])
	if vals != 0:
		Sum += cond(vals)

print(Sum)

