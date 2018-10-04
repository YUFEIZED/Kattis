#! /usr/bin/python3
from puzzle import Puzzle
from sudoku import Sudoku
import time
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (function, str(t1-t0))
               )
        return result
    return function_timer

@fn_timer
def test():
	#newPuzzle = [[],[],[],[],[],[],[],[],[]]
	
	oldPuzzleCells1 = [[9,6,3,1,7,4,2,4,8],[1,7,8,3,2,5,6,4,9],[2,5,4,6,8,9,7,3,1],[8,2,1,4,3,7,5,9,6],[4,9,6,8,5,2,3,1,7],[7,3,5,9,6,1,8,2,4],[5,8,9,7,1,3,4,6,2],[3,1,7,2,4,6,9,8,5],[6,4,2,5,9,8,1,7,3]]
	newPuzzleCells1 = [[0,6,0,1,0,4,0,4,0],[2,0,0,0,0,0,0,0,1],[0,0,8,3,0,5,6,0,0],[8,0,0,4,0,7,0,0,6],[0,0,6,0,0,0,3,0,0],[7,0,0,9,0,1,0,0,4],[5,0,0,0,0,0,0,0,2],[0,4,0,5,0,8,0,7,0],[0,0,7,2,0,6,9,0,0]]
	oldPuzzle1 = Puzzle(oldPuzzleCells1)
	newPuzzle1 = Puzzle(newPuzzleCells1)
	Sudoku1 = Sudoku(oldPuzzle1, newPuzzle1)
	compareRes1 = Sudoku1.comparePuzzle()
	print (compareRes1)
	
	oldPuzzleCells2 = [[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
	newPuzzleCells2 = [[0,1,0,9,0,0,6,0,5],[0,2,5,0,6,0,0,7,0],[8,7,0,0,0,0,9,0,2],[7,0,2,0,5,0,0,4,3],[0,0,0,2,0,4,0,0,0],[4,9,0,0,1,0,5,0,8],[1,0,7,0,0,0,0,5,6],[0,4,0,0,8,0,2,1,0],[2,0,8,0,0,1,0,9,0]]
	oldPuzzle2 = Puzzle(oldPuzzleCells2)
	newPuzzle2 = Puzzle(newPuzzleCells2)
	Sudoku2 = Sudoku(oldPuzzle2, newPuzzle2)
	compareRes2 = Sudoku2.comparePuzzle()
	print (compareRes2)

def main():
	numOfCompare = int(input().split()[0])
	oldPuzzleCells = [[0 for x in range(9)] for y in range(9)] 
	newPuzzleCells = [[0 for x in range(9)] for y in range(9)] 
	for num in range(numOfCompare):
		for i in range(9):
			oldPuzzleRow = input().split()[0]
			for j in range(9):
				oldPuzzleCells[i][j] = int(oldPuzzleRow[j])
		for i in range(9):
			newPuzzleRow = input().split()[0]
			for j in range(9):
				newPuzzleCells[i][j] = int(newPuzzleRow[j])
		oldPuzzle = Puzzle(oldPuzzleCells)
		newPuzzle = Puzzle(newPuzzleCells)
		SudokuRes = Sudoku(oldPuzzle, newPuzzle)
		resOfCompare = SudokuRes.comparePuzzle()
		print (resOfCompare)
		if num < numOfCompare-1:
			removeBlankLine = input().split()
"""
def test3(old,new,colSeg):
	flag = []
	for col in range(colSeg*3, colSeg*3+3):
		flag.append([])
		for colNew in range(colSeg*3, colSeg*3+3):
			for row in range(9):
				if new[row][colNew] != 0 and new[row][colNew] != old[row][col]:
					flag[col%3].append(0)
					break
			if len(flag[col%3]) != colNew%3 + 1:
				print ("test")
				flag[col%3].append(1)
			print (flag)
			print (colNew)
		if sum(flag[col%3]) == 0:
			print (flag)
			return False
	print (flag)
	return True

def test2():
	old = [[9,6,3],[1,7,8],[2,5,4],[8,2,1],[4,9,6],[7,3,5],[5,8,9],[3,1,7],[6,4,2]]
	new = [[0,6,0],[0,0,0],[0,0,4],[8,0,0],[0,0,6],[7,0,0],[5,0,0],[0,1,7],[6,0,2]]
	#old = [[9,6,3,1,7,4,2,4,8],[1,7,8,3,2,5,6,4,9],[2,5,4,6,8,9,7,3,1],[8,2,1,4,3,7,5,9,6],[4,9,6,8,5,2,3,1,7],[7,3,5,9,6,1,8,2,4],[5,8,9,7,1,3,4,6,2],[3,1,7,2,4,6,9,8,5],[6,4,2,5,9,8,1,7,3]]
	#new = [[0,6,0,1,0,4,0,4,0],[2,0,0,0,0,0,0,0,1],[0,0,8,3,0,5,6,0,0],[8,0,0,4,0,7,0,0,6],[0,0,6,0,0,0,3,0,0],[7,0,0,9,0,1,0,0,4],[5,0,0,0,0,0,0,0,2],[0,4,0,5,0,8,0,7,0],[0,0,7,2,0,6,9,0,0]]
	
	colSeg = 0

	res = test3(old, new, colSeg)
	print (res)
"""

if __name__ == "__main__":
	test()

