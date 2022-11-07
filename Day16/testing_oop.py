# import another_module
#
# print(another_module.another_variable)

# import turtle
#
# tonny = turtle.Turtle()

# TODO: "or"

# from turtle import Turtle, Screen
#
# # object is being printed
# tonny = Turtle()
# print(tonny)
# tonny.color("DeepPink3")
# tonny.shape("turtle")
# tonny.forward(100)
#
# my_screen = Screen()
# # my_screen is an object of Screen where it can access attributes
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]), table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
