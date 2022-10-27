class person:


    __name   = "No Name"
    __age    = 0
    __height = 0.0


    def __init__(self):
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
            del  self.__name


        @property
        def Age(self):
            return self.__age

        @Age.setter
        def Age(self,value):
           self.__age=value

           
         @Age.deleter 
         def Age(self):
             del self.__age

        @property
        def Height(self):
            return self.__height


        @Height.setter
        def Height(self,value):
           self.__height=value

        @Height.deleter
         def Height(self):
             del self.__height




person1=person()
person1.Name   = "Frank"
person1.Age    = 19
person1.Height = 162
print("name     : {0}"              .format(Person1,Name))
print("age      : {0}" years old    .format(Person1,Age))
print("Height   : {0}" cm             .format(Person1,Height))


        
person2=person()
person2.Name   = "Ronald"
person2.Age    = 25
person1.Height = 174
print("name     : {0}"              .format(Person2,Name))
print("age      : {0}" years old    .format(Person2,Age))
print("Height   : {0}" cm             .format(Person2,Height))


                
        
        
            
