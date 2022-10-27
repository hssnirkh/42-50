class Parent:
    def __init__(self,m):
        self.message = m
        
    @property
    def Message(self):
        return self.message
    @Message.setter
    def Message(self,value):
        self.message = value
    def showmessage (self):
        print(self.message)
        
class Child(Parent):
    def __init__(self,m):
        super().__init__(m)

class GrandChild(Child):
    pass

myParent = Parent("Message from parent.")
myChild  = Child("Message from Child.")
myGrandChild = GrandChild("Message from GrandChild.")

myParent.showmessage ()
myChild.showmessage ()
myGrandChild.showmessage ()

print()

myParent.Message = "Modified message of the parent."
myParent.showmessage ()


myChild.Message = "Modified message of the child."
myChild.showmessage ()