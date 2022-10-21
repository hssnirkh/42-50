def testreturnexit():
    print("Line 1 inside the method testreturnexit()")
    print("Line 2 inside the method testreturnexit()")
    return

   #The following lines will not execute
    print("Line 3 inside the method testreturnexit()")
    print("Line 4 inside the method testreturnexit()")

testreturnexit()
print("Hello world!")
