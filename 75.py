#75
class persion:
	name = ""
	age = 0
	heiht = 0
	def tellInformation(self):
		print("name : {0}".format(self.name))
		print("age : {0}".format(self.age))
		print("height : {0}".format(self.height))

firstPersion = persion()
secondPersion = persion()

firstPersion.name = "jack"
firstPersion.age = 21
firstPersion.height = 160
firstPersion.tellInformation()

print()

secondPersion.name = "mike"
secondPersion.age = 23
secondPersion.height = 158
secondPersion.tellInformation()

