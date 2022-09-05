age = int(input("Enter your age: "))
gen = input("male of female: ") 

if (age > 12):
	if(age < 20):
		if(gen == "male"):
			print("tenage boy")
		else:
			print("tenager girl")
	else: 
		print("adult")
else:
	print("too young")
