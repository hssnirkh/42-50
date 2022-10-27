class Parent:
    def showmessage (self):
        print("Message from Parent.")
        
class Child(Parent):
    def showmessage (self):
        super().showmessage ()
        print("showmessage method was overrided !")
        
myChild = Child()
myChild.showmessage ()