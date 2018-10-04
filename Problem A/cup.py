class Cup:
	def __init__(self,color,rad):
		self.color = color
		self.rad = rad
	def __getattr__(self, key):
		if key == 'color':
			return self.color
		if key == 'rad':
			return self.rad
