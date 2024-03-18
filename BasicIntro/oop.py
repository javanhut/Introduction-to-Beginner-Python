"""
Object-oriented programming has 4 major components:
1.Polymorphism
2.Abstraction
3.Encapsulation
4.Inheritance
"""
#Inheritance
# class Food:
#     def __init__(self, name, food_group):
#         self.name = name
#         self.food_group = food_group
#
#     def name_and_food_group(self):
#         print(f"The name of this food is {self.name} and it belongs to food group {self.food_group}")
#
#     def get_name(self):
#         return self.name
#
#     def get_food_group(self):
#         return self.food_group
#
# class Pizza(Food):
#
#     def __init__(self, name, food_group):
#         super().__init__(name=name, food_group=food_group)
#
# pizza = Pizza("pepperoni", "grains")
# pizza.name_and_food_group()
# print(pizza.get_name())
# print(pizza.get_food_group())

#Encapsulation
# class Food:
#
#     def __init__(self):
#         #public attribute
#         self.grains = "Bread"
#         #protected attribute
#         self._fruits = "Apple"
#         #private attribute
#         self.__meat = "Steak"
#
#     def get_meat(self):
#         return self.__meat
#
#     def set_meat(self, meat_name):
#         self.__meat = meat_name
#
# food_1 = Food()
# print(food_1.grains)
# print(food_1._fruits)
# print(food_1.get_meat())
# food_1.set_meat("Chicken")
# print(food_1.get_meat())

#Abstraction
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     def __init__(self, name, species):
#        pass
#     @abstractmethod
#     def name(self):
#         pass
#
#     @abstractmethod
#     def species(self):
#         pass
#
#
#     @abstractmethod
#     def species_and_name(self):
#         pass
#
#
# class Mammal(Animal):
#     def __init__(self, name, species):
#         self.__name = name
#         self.__species = species
#
#     def name(self):
#         return self.__name
#
#     def species(self):
#         return self.__species
#
#     def species_and_name(self):
#         print(f"The name of this animal is {self.__name} and the species is {self.species()}")
#
#
# a1 = Mammal(name="Lassie", species="Dog")
# print(a1.name())
# print(a1.species())
# a1.species_and_name()

#Polymorphism
# class Duck:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"The duck named {self.name} says quacks")
#
#     def walk(self):
#         print(f"The duck named {self.name} waddles")
# class Chicken:
#
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"The chicken named {self.name} says clucks")
#
#     def walk(self):
#         print(f"The chicken named {self.name} walks like chicken")
#
# def action(obj: Duck) -> None:
#     obj.speak()
#     obj.walk()
#
# duck = Duck("Daffy")
# chicken = Chicken("Arnold")
#
#
# action(chicken)