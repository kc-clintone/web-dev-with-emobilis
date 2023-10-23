class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} is barking!"

my_dog = Dog("Buddy", "Labrador")
print(my_dog.bark())  # Output: "Buddy is barking!"
