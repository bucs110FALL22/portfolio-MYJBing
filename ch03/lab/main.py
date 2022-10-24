import turtle #1. import modules
import random
import pygame
import math


#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here #My Code
# Each tutle forward
michelangelo.forward(random.randrange(1,101,1))
leonardo.forward(random.randrange(1,101,1))

#Reset Turtle Position
michelangelo.goto(-100,20)
leonardo.goto(-100,20)
michelangelo.up()
leonardo.up()

#New race length for each turtle for loop operation
#randomrange(0,10)

for i in range(10):
  michelangelo.forward(random.randrange(0,10))
  leonardo.forward(random.randrange(1,10,1))

#Reset
michelangelo.setposition(-100,20)
leonardo.setposition(-100,20)

window.exitonclick

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()
pygame.display.flip()

# Triangle
coords = []
num_sides = 3
side_length = 300
offset = 200 
for i in range(num_sides):
  theta = 2.0*math.pi* i/num_sides
  x = side_length *math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))  

pygame.draw.polygon(window, 'green', coords)
pygame.display.flip()
pygame.time.delay(1000)
window.fill('red')


#Hexagon
coords= []
num_sides = 6
for i in range(num_sides): 
  theta = 2.0*math.pi* i/num_sides
  x =  side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window, 'red', coords)
pygame.display.flip()
pygame.time.delay(1000)
window.fill('grey')

  #Square 
coords= []
num_sides= 4
for i in range(num_sides):
    theta = 2.0*math.pi * i + offset
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x, y))

pygame.draw.polygon(window, "blue", coords)
pygame.display.flip()
pygame.time.delay(1000)
window.fill("red")

#nonagon
coords= []
num_sides = 9
for i in range(num_sides):
    theta = 2.0*math.pi * i + offset
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x, y))

    
pygame.draw.polygon(window, 'black', coords)
pygame.display.flip()
pygame.time.delay(1000)
window.fill('gold')

#circle
coords= []
num_sides= 360
for i in range(num_sides):
    theta = 2.0*math.pi * i + offset
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x, y))

pygame.draw.polygon(window, 'yellow', coords)
pygame.display.flip()
pygame.time.delay(1000)
window.fill('black')

pygame.display.update

window.exitonclick()
