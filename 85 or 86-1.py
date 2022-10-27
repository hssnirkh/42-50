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
        
myParent = Parent("Message from parent.")
myChild  = Child("Message from Child.")

myParent.showmessage ()
myChild.showmessage ()

myParent.Message = "Modified message of the parent."
myParent.showmessage ()
              