class Animal:
    pass
class Dog(Animal):
    pass
myAnimal = Animal()
if type(myAnimal) is Animal:
    print("myAnimal is an Animal!")