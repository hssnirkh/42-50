def functionA(myFunction):
    return myFunction()

def functionB():
    return "Hello world!"

print("{0}".format(functionA(functionB)))
