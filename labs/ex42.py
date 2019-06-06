## Animal is-a object
class Animal(object):
    pass

## sets an animal to the class
class Dog(Animal):
    
    def __init__(self, name):
        ## sets the self name to the name
        self.name = name
        
## adds an animal to the the class
class Cat(Animal):
    
    def __init__(self, name):
        ## sets the self name to the name
        self.name = name
        
## creates a new class
class Person(object):
    
    def __init__(self, name):
        ## sets the self name to the name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None

## creates a sub class
class Employee(Person):
    
    def __init__(self, name, salary):
        ## returns the variable
        super(Employee, self).__init__(name)
        ## defines salary
        self.salary = salary
        
## defines fish as an object
class Fish(object):
    pass

## defines salmon as a fish
class Salmon(Fish):
    pass

## defines Halibut as a fish
class Halibut(Fish):
    pass


## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary's pet is satan
mary.pet = satan

## defines Franks salary
frank = Employee("Frank", 120000)

# frank's pet is rover
frank.pet = rover

## sets the name for the fish
flipper = Fish()

## ?
crouse = Salmon()

# ?
harry = Halibut()