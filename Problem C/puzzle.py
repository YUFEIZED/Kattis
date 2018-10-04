class Puzzle:
	def __init__(self,cells):
		self.cells = cells

	def __getattr__(self, key):
		if key == 'cells':
			return self.cells

	def getPuzzel(self):
		return self.cells

	def swapRow(self, first, second):
		for col in range(9):
			tmp = self.cells[first][col]
			self.cells[first][col] = self.cells[second][col]
			self.cells[second][col] = tmp

	def swapCol(self, first, second):
		for row in range(9):
			tmp = self.cells[row][first]
			self.cells[row][first] = self.cells[row][second]
			self.cells[row][second] = tmp

	def swapRowSeg(self,first,second):
		for row in range(3):
			for col in range(9):
				tmp = self.cells[first*3 + row][col]
				self.cells[first*3 + row][col] = self.cells[second*3 + row][col]
				self.cells[second*3 + row][col] = tmp

	def swapColSeg(self,first,second):
		for col in range(3):
			for row in range(9):
				tmp = self.cells[row][first*3 + col]
				self.cells[row][first*3 + col] = self.cells[row][second*3 + col]
				self.cells[row][second*3 + col] = tmp

	def rotateClockwise(self):
		rotated = list(zip(*self.cells[::-1]))
		self.cells = [list(row) for row in rotated]

	#def rotateCounterClockwise(self):
	#	rotated = np.rot90(self.cells, 1)
	#	self.cells = rotated

	def colSegSwapCompare1(self,puzzle,colSeg):
		flag = []
		for col in range(colSeg*3, colSeg*3+3):
			flag.append([])
			for colNew in range(colSeg*3, colSeg*3+3):
				for row in range(9):
					if puzzle.cells[row][colNew] != 0 and puzzle.cells[row][colNew] != self.cells[row][col]:
						flag[col%3].append(0)
						break
				if len(flag[col%3]) != colNew%3 + 1:
					flag[col%3].append(1)
			if sum(flag[col%3]) == 0:
				return False
		return True	
		flag2 = 0
		for i in range(3):
			if sum(row[i] for row in flag) == 0:
				flag = 1
				break
		if flag == 1:
			return False
		return True

	def colSegSwapCompare(self, puzzle, colSeg):
		for seg in range(6):
			if self.colSegCompare(puzzle,colSeg):
				return True
			if seg%2 == 0:
				self.swapCol(colSeg*3+1, colSeg*3+2)
			else:
				self.swapCol(colSeg*3+0, colSeg*3+2)
		return False
		
	def colSegCompare(self, puzzle, colSeg):
		for row in range(9):
			for col in range(colSeg*3, colSeg*3+3):
				if puzzle.cells[row][col] != 0 and puzzle.cells[row][col] != self.cells[row][col]:
					return False
		return True

	






