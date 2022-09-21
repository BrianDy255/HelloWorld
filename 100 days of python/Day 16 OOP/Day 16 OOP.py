# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# turtle.color('coral')
# turtle.forward(200)
# turtle.left(130)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = "l"
print(table)