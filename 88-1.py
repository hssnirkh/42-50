class A:
    def AMessage(self):
        print("Message from A.")
        
class B:
    def BMessage(self):
        print("Message from B.")
        
class C:
    def CMessage(self):
        print("Message from C.")
        
class D(A,B,C):
    pass

d = D()

d.AMessage()
d.BMessage()
d.CMessage()
         