import numpy as np

data = np.genfromtxt("Day1Data.txt")

for i in range(200):
	for j in range(200):
			for k in range(200):
				if data[i]+data[j]+data[k]==2020:

					print(data[i]*data[j]*data[k])