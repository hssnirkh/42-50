class Test:
    def addfive(self,number):
        number = number + self.five
        return number 
    
x = Test()
x.five = 10
print(x.addfive(100))
