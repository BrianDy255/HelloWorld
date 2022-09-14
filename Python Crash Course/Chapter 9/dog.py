class Dog:
    """A simple attempt to model a dog"""
    def __init__(self,name,age):
        """initialize name and attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command."""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f'{self.name} is rolling over.')

my_dog = Dog('Willie', 3)
print(f' My dogs name is {my_dog.name}')
print(f' {my_dog.name}s age is {my_dog.age} years old ')

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Mimi', 16)
print(f"Your dog's name is {your_dog.name} and she's {your_dog.age}"
      f" years old. {your_dog.name}" )

your_dog.sit()