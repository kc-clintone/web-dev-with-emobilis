class Students:
	def __init__(self, name, course, gender, age):
		self.name=name
		self.course=course
		self.gender=gender
		self.age=age
	def mfn(self):
		print("Name: %s \nCourse: %s \nGender: %s Age: %d" % (self.name, self.course, self.gender, self.age))

obj = mfn("clinton", "hp", "male", 88)
