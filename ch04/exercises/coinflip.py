import turtle
import random

window = turtle.Screen()
window.bgcolor("yellow")
window.setup( width = 300, height = 300)

joy = turtle.Turtle()
joy.shape("turtle")
joy.color("red")

x = 0
y = 0 

joy.goto(x, y)

coin= ['heads','tails']

is_in_window= True

while is_in_window:
  result = random.choice(coin)

  x_range = window.window_width()/2
  y_range = window.window_height()/2

  if (result == 'heads'):
    print(result)
    joy.left(90)
    joy.forward(50)
    x = joy.xcor()
    y = joy.ycor()
    print("(x,y)")

  elif (result == 'tails'):
    print(result)
    joy.right(90)
    joy.forward(50)
    x = joy.xcor()
    y = joy.ycor()
    print("(x,y)")


if abs(x) > 150 or abs(y) > 150:
   is_in_window = False

window.exitonclick()

#Done
    

