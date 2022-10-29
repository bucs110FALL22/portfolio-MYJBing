import turtle

cheerful = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('aqua')
screen.screensize(500, 500)

turtle.title("My Cheerful Turtle")

eyeleftx = -20
eyelefty = 10
eyerightx = 20
eyerighty = 10

clouda1x = -100
clouda1y = 300
clouda2x = -50
clouda2y = 300
clouda3x = 0
clouda3y = 300

cloudb1x = 100
cloudb1y = 200
cloudb2x = 150
cloudb2y = 200
cloudb3x = 200
cloudb3y = 200

def main():
    ground()
    sun()
    cloud(clouda1x,clouda1y)
    cloud(clouda2x,clouda2y)
    cloud(clouda3x,clouda3y)
    cloud(cloudb1x,cloudb1y)
    cloud(cloudb2x,cloudb2y)
    cloud(cloudb3x,cloudb3y)
    face()
    eyes(eyeleftx,eyelefty)
    eyes(eyerightx,eyerighty)
    smile()

    screen.exitonclick()

def face():
    '''
    This creates the face of the smiley face using turtle modules.

    Args:

    Return:
    This returns a gold circle for the face.
    '''
    cheerful.penup()
    cheerful.goto(0,-50)
    cheerful.pendown()
    cheerful.fillcolor('gold')
    cheerful.begin_fill()
    cheerful.circle(50)
    cheerful.end_fill()
    cheerful.penup()

def eyes(x,y):
    '''
    This creates a black circle for the face

    Args:
    x: coordinate for where the eye will be
    y: coordinate for where the eye will be

    Return:
    Gives a black circle for eyes
    '''
    cheerful.penup()
    cheerful.goto(x, y)
    cheerful.pendown()
    cheerful.fillcolor('black')
    cheerful.begin_fill()
    cheerful.circle(5)
    cheerful.end_fill()
    cheerful.penup()

def smile():
    '''
    This creates the smile utilizing turtle modules

    Args:

    Return:
    Creates the smile for the face
    '''
    cheerful.goto(-20,-20)
    cheerful.pendown()
    cheerful.goto(-20,-30)
    cheerful.goto(20,-30)
    cheerful.goto(20,-20)
    cheerful.penup()
    cheerful.goto(0,0)
    cheerful.lt(90)

def sun():
    '''
    This creates a sun

    Args:

    Return:
    Creates a yellow circle to represent the sun
    '''
    cheerful.penup()
    cheerful.goto(-300,300)
    cheerful.pendown()
    cheerful.fillcolor('yellow')
    cheerful.begin_fill()
    cheerful.circle(100)
    cheerful.end_fill()

def ground():
    '''
    This creates green land

    Args:

    Return:
    Creates a green patch of land at the bottom half of the screen
    '''
    cheerful.penup()
    cheerful.goto(-500,0)
    cheerful.pendown()
    cheerful.fillcolor('green')
    cheerful.begin_fill()
    cheerful.goto(500,0)
    cheerful.goto(500,-500)
    cheerful.goto(-500,-500)
    cheerful.goto(-500,0)
    cheerful.end_fill()

def cloud(x,y):
    '''
    This creats individual circles for parts of a cloud

    Args:
    x: coordinate for the cloud
    y: coordinate for the cloud

    Return:
    Creates one white circle for a part of the cloud
    '''
    cheerful.penup()
    cheerful.goto(x,y)
    cheerful.pendown()
    cheerful.fillcolor('white')
    cheerful.begin_fill()
    cheerful.circle(50)
    cheerful.end_fill()
main()



