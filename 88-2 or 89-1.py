class Parent:
    def showmessage (self):
        print("Message from Parent.")
        
class Child(Parent):
    def showmessage (self):
        print("Message from Child.")
        
myChild = Child()
myChild.showmessage ()