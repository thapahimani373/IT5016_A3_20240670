class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")  # Base method for all animals.

class Dog(Animal):  # Inherits from Animal.
    def speak(self):
        print(f"{self.name} says Woof!")  # Changes the sound – reuse with a twist.

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Analysis: Inheritance lets me reuse Animal code for Dog and Cat. It’s easy to extend – I could add Bird later. I found this interesting because it saves time but needs care to avoid confusion.
dog = Dog("Max")
cat = Cat("Luna")
dog.speak()
cat.speak()
