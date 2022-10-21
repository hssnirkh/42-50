class person:
	#constructor
	def __init__(self,n = "",a = 0,h = 0):
		self.name = n
		self.age = a
		self.height = h
	def showInformation(self):
		print("name : {0}:".format(self.name))
		print("age : {0}:".format(self.age))
		print("height : {0}:".format(self.height))

firstPersion = person()
firstPersion.name = "hassan"
firstPersion.age = 30
firstPersion.height = 180
firstPersion.showInformation()

print()

secondPersion = person("reza",28,170)
secondPersion.showInformation()
