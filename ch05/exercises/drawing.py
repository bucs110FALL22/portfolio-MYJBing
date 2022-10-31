import turtle


def drawEqShape(myturtle, num_sides, side_length):
  angle = (360 /num_sides)
  for i in range(num_sides):
    myturtle.forward(side_length)
    myturtle.left(angle)


myturtle = turtle.Turtle()
myturtle.shape("turtle")
myturtle.color("green")
num_sides = int(input("Enter number of sides: "))
side_length = int(input("Enter side length: "))

drawEqShape(myturtle, num_sides , side_length)



