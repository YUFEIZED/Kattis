from puzzle import Puzzle

class Sudoku:
	def __init__(self,oldPuzzle,newPuzzle):
		self.oldPuzzle = oldPuzzle
		self.newPuzzle = newPuzzle
		self.compareRes = False
		
	def __getattr__(self, key):
		if key == 'oldPuzzle':
			return self.oldPuzzle
		if key == 'newPuzzle':
			return self.newPuzzle
		if key == 'compareRes':
			return self.compareRes

	def comparePuzzle(self):
		for rot in range(3):
			for rowSeg in range (6):
				for row0 in range (6):
					for row1 in range (6):
						for row2 in range (6):
							for colSeg in range(6):	
								if self.oldPuzzle.colSegSwapCompare(self.newPuzzle, 0):
									if self.oldPuzzle.colSegSwapCompare(self.newPuzzle, 1):
										if self.oldPuzzle.colSegSwapCompare(self.newPuzzle, 2):
											self.compareRes = True
											return 'Yes'
								if colSeg%2 == 0:
									self.oldPuzzle.swapColSeg(1,2)
								else:
									self.oldPuzzle.swapColSeg(0,2)
							if row2%2 == 0:
								self.oldPuzzle.swapRow(7,8)
							else:
								self.oldPuzzle.swapRow(6,8)
						if row1%2 == 0:
							self.oldPuzzle.swapRow(4,5)
						else:
							self.oldPuzzle.swapRow(3,5)
					if row0%2 == 0:
						self.oldPuzzle.swapRow(1,2)
					else:
						self.oldPuzzle.swapRow(0,2)
				if rowSeg%2 == 0:
					self.oldPuzzle.swapRowSeg(1,2)
				else:
					self.oldPuzzle.swapRowSeg(0,2)
			self.oldPuzzle.rotateClockwise();
		#self.compareRes = False
		return 'No'


