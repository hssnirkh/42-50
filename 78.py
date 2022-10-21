class person:
        #constructor
        def __init__(self,n = "",a = 0,h = 0):
                self.name = n
                self.age = a
                self.height = h
        def showInformation(self):
                print("name : {0}:".format(self.name))
                print("age : {0}:".format(self.age))
                print("height : {0}:".format(self.height))

firstPersion = person()
secondPersion = person("jack")
thirdPersion = person("mike",23)
forthPersion = person("chris",25,178)

firstPersion.showInformation()
secondPersion.showInformation()
thirdPersion.showInformation()
forthPersion.showInformation()

