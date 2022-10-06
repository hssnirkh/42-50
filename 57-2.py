def getnumber():
    number = int(input("Enter a number greater than 10: "))
    if number > 10:
        return number
    else:
        return 0

result = getnumber()

print("Result = {0}.".format(result))
        
