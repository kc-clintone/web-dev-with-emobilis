class Cars:
	def __init__(self, type, color, model):
		self.type = type
		self.color = color
		self.model = model

	def show(self):
		print(f"{self.type},{self.color},{self.model}")
