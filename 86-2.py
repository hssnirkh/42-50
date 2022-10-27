class Parent:
    def __init__(self):
        print("Parent Constructor!")
        
class Child(Parent):
    def __init__(self):
        print("Child Constructor!")
        super().__init__()
        
myChild = Child()        