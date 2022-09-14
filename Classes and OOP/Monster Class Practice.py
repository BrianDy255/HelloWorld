class Monster:

    def __init__(self, health, energy):
        print('The monster was Created.')
        self.health = health
        self.energy = energy

    def __call__(self):
        return "The Monster was called"

    def __add__(self, other):
        print(f' {self.health + other} added')

    def __str__(self):
        return f' A monster with {self.health} health and {self.energy} energy'

    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} has been dealt')
        self.energy -= 20
        print(self.energy)

    def move(self, mv_amnt):
        print('THe monster has moved')
        print(f' The monster moved {mv_amnt}')
        self.speed += int(2)
        print(self.speed)


monster1 = Monster(10, 20)
print(vars(monster1))
print(monster1())
print(monster1 + 20)
print(monster1)