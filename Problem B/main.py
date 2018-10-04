#! /usr/bin/python3

class InputFile:
	def __init__(self,file):
		self.file = file
		self.hash = fileToHash(file)
	def __str__(self):
		return self.file
	def __getattr__(self, key):
		if key == 'file':
			return self.file
		if key == 'hash':
			return self.hash

def fileToAscII(file):
	res = []
	for c in file:
		res.append(ord(c))
	return res

def hashFunc(ascList):
	if len(ascList)>0:
		res = ascList[0]
		for i in range(1,len(ascList)):  # get the exclusive of(XOR) of the ASCII value
			res = res ^ ascList[i]
		return res		

def fileToHash(file):
	ascList = fileToAscII(file)
	hashing = hashFunc(ascList)
	return hashing

def main():
	while(1):
		numOfFiles = int(input().split()[0])
		if numOfFiles==0:
			break
		inputDict = {}
		for i in range(numOfFiles):
			file = input().splitlines()[0]
			inputFile = InputFile(file)
			if inputFile.hash in inputDict:
				inputDict[inputFile.hash].append(inputFile.file)
			else: 
				inputDict[inputFile.hash] = []
				inputDict[inputFile.hash].append(inputFile.file)

		numOfUniqueFiles = 0
		numOfHashCollisions = 0
		for k in inputDict.keys():
			numOfUniqueFiles += len(set(inputDict[k]))
			length = len(inputDict[k])
			if length > 1:
				for i in range(length-1):
					for j in range(i+1, length):
						if (inputDict[k][i] != inputDict[k][j]):
							numOfHashCollisions += 1
		print (numOfUniqueFiles, numOfHashCollisions)
		continue

if __name__ == "__main__":
	main()


