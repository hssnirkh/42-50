class Person:
    __name   = "No Name"
    __age    = 0
    __height = 0.0
    
    def __init__ (self):
        self.__name
        self.__age
        self.__height
        @property
        def Name(self):
            return self.__name
        @Name.setter
        def Name(self,value):
            self.__name = value
        @Name.deleter
        def Name(self):
            del self.__name
        @property
        def Age(slfe):
            return selfe.__age
        @Age.setter
        def Age(self,value):
            self.__age = value
        @Age.deleter
        def Age(self):
            del self.__age
        @property
        def Height(self):
            return self.__age
        @Height.setter
        def Height(self,value):
            self.__height = value
        @Height.deleter
        def Height(self):
            del self.__height
            
person1        = Person()
person1.Name   = "Frank"
person1.Age    = 19
person1.Height = 162
print("name  : {0}"           .format(person1.Name))
print("age   : {0} years old" .format(person1.Age))
print("height : {0}cm"        .format(person1.Height))

print()#Seperator

person2 = Person()
person2.Name = "Ronald"
person2.Age = 25
person2.Height = 174
print("name  : {0}"           .format(person2.Name))
print("age   : {0} years old" .format(person2.Age))
print("height : {0}cm"        .format(person2.Height))
