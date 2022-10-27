class Animal:
    pass
class Dog(Animal):
    pass
myDog = Dog()

if isinstance(myDog, Animal):
    print("myDog ia an Animal!")