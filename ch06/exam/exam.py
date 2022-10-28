import turtle
import colorsys

screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty= 100)

# turtle object
happypen= turtle.Turtle()

 # function for eye
def eye(col, rad):
  happypen.down()
  happypen.fillcolor(col)
  happypen.circle(rad)
  happypen.end_fill()
  happypen.up()

  # Face Construction
happypen.fillcolor('yellow')
happypen.begin_fill()
happypen.circle(150)
happypen.end_fill()
happypen.up()

# eye construction
happypen.goto(-40, 120)
eye('white', 15)
happypen.goto(-37, 125)
eye('black', 5)
happypen.goto(40, 120)
eye('white', 15)
happypen.goto(40, 125)
eye('black',5)

# nose construction
happypen.goto(0, 75)
eye('black', 8)

# mouth
happypen.goto(-40, 85)
happypen.down()
happypen.right(90)







