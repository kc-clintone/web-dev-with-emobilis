#Polymorphism allows different objects to respond to the same method call in
#a way that's appropriate for their specific class. It's achieved through method overriding.


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_sound(dog))  # Output: "Woof!"
print(animal_sound(cat))  # Output: "Meow!"

