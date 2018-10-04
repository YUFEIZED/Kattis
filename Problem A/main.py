#! /usr/bin/python3
# Cup stacking module: 
# Glitch: red 5 o== 10 red
# Method of sorting here:
# Timsort: a hybrid stable sorting algorithm, derived from merge sort and insertion sort. If the input data is closed to the ordered data, means much better result. 
# worst-case performance: O(nlogn); best-case performance: O(n)
# use insertion sort to combine runs smaller than the minimum run size, and merge sort otherwise
# first search the ordered minimum-size sequences. If the length a is smaller than minimum size b, use insertion sort to insert x(x = b-a) elements to the run. 
# Then push to stack. Use merge sort to compare run1, run2, run3....
# Exponential search, A = [101 102 ... 200], B = [1 2 3 .. 100]. If only use merge sort, compare first element when iterating the run1. So exponential search is used
# Which is called Gallop. 0,0; 0,1; 0,3; 0,7; 0,15; 2^n-1

class Cup:
	def __init__(self,color,rad):
		self.color = color
		self.rad = rad
	def __getattr__(self, key):
		if key == 'color':
			return self.color
		if key == 'rad':
			return self.rad

def main():
	numOfCups = int(input().split()[0])
	cup_list = []
	for x in range(numOfCups):
		strList = input().split()
		if strList[0].isdigit() == False and strList[1].isdigit() == True:
			cup_list.append(Cup(strList[0],int(strList[1])))
		else:
			cup_list.append(Cup(strList[1],int(strList[0])*0.5))
	cup_list.sort(key=lambda x: (x.rad))
	for cup in cup_list:
		print (cup.color)

if __name__ == "__main__":
	main()
