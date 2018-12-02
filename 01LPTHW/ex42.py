## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a init
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a init
        self.name = name

## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## person has-a init
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?it has three params?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary


## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## from mary,get the pet attribute, and set it to satan
mary.pet = satan

## set frank to an instance of class Employee
frank = Employee("Frank", 120000)

## from frank, get the pet attribute, and set it to rover
frank.set = rover

## set flipper to an instance of class Fish
flipper = Fish()

## set crouse to an instance of class Salmon
crouse = Salmon()

## set harry to an instance of class Halibut
harry = Halibut()