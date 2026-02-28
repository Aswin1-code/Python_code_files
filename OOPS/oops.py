from abc import ABC, abstractmethod

# Class and Object
class SimpleCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Encapsulation
class EncapsulatedCar:
    def __init__(self, make, model, year):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.__make} {self.__model}")

    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

# Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Polymorphism
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):

    def make_sound(self):
        return "Meow!"

# Abstraction
class AbstractAnimal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class AbstractDog(AbstractAnimal):
    def make_sound(self):
        return "Woof!"

class AbstractCat(AbstractAnimal):
    def make_sound(self):
        return "Meow!"

# Main function to demonstrate the concepts
def main():
    # Class and Object
    my_car = SimpleCar("Toyota", "Corolla", 2020)
    my_car.display_info()

    # Encapsulation
    my_encapsulated_car = EncapsulatedCar("Honda", "Civic", 2021)
    my_encapsulated_car.display_info()
    print(my_encapsulated_car.get_make())
    my_encapsulated_car.set_make("Ford")
    my_encapsulated_car.display_info()

    # Inheritance
    my_vehicle = Vehicle("Generic", "Model")
    my_vehicle.display_info()
    my_inherited_car = Car("Tesla", "Model S", 2022)
    my_inherited_car.display_info()

    # Polymorphism
    dog = Dog()
    cat = Cat()
    print(dog.make_sound())
    print(cat.make_sound())

    # Abstraction
    abstract_dog = AbstractDog()
    abstract_cat = AbstractCat()
    print(abstract_dog.make_sound())
    print(abstract_cat.make_sound())

if __name__ == "__main__":
    main()