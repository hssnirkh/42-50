class test:
	def __init__(self):
		print("constructor was called")
	def __del__(self):
		print("Destructor was called")

x1 = test()
del x1

