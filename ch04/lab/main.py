import pygame
import random
import math
import time
import os

#Part A
pygame.init()

window = pygame.display.set_mode((300, 300))
window_dimension = pygame.display.get_window_size()
window.fill('aqua')

#Window Height = 300, #Window Width = 300

dartboard = pygame.draw.circle(window, 'gold', (150, 150), 150)
pygame.draw.line(window, 'black', (0, 150), (300, 150), 1)
pygame.draw.line(window, 'black', (150, 0), (150, 300), 1)
pygame.display.flip()
#Center = (150, 150)

#Part B

for i in range(10):
    x = random.randrange(0, 300)
    y = random.randrange(0, 300)
    coords = [x, y]
    print(coords)

for i in [coords]:
    distance_from_center = math.hypot(x - 150, y - 150)
is_in_circle = distance_from_center <= 300 / 2

if is_in_circle == True:
    pygame.draw.circle(window, 'green', (coords), (3))

if is_in_circle == False:
    pygame.draw.circle(window, 'magenta', (coords), (3))

pygame.display.flip()

#Part C
pygame.time.delay(4000)
windowC = pygame.display.set_mode([300, 300])
windowC.fill('lime')

player_red = pygame.draw.rect(windowC, 'red', pygame.Rect(0, 0, 150, 300))
player_blue = pygame.draw.rect(windowC, 'blue', pygame.Rect(0, 0, 150, 300))

pygame.display.flip()

Player_blue_score = 0 #null
Player_red_score = 0   #null


player_selected = ""

player_chosen = False
while not player_chosen:
  for event in pygame.event.get(): 
     if event.type == pygame.MOUSEBUTTONUP:
       (xmouse, ymouse) = pygame.mouse.get_pos()
       if player_red.collidepoint(xmouse, ymouse):
        print("Guess who will win?")
        player_selected = 'red'
        player_chosen = True
       pygame.display.flip()

     else:
       print('Guess who will win?')
       player_selected = 'blue'
       player_chosen = True
       pygame.display.flip

windowA =pygame.display.set_mode([300, 300])
windowA.fill('blue')
pygame.draw.circle(windowA, 'brown', (150, 150), (150))
pygame.draw.line(windowA, 'black', (0,150), (300, 150))
pygame.draw.line(windowA, 'black', (0,150), (300, 150))
pygame.display.flip()



for i in range(10):
    x = random.randrange(0, 300)
    y = random.randrange(0, 300)
    coords = [x, y]
  
    pygame.draw.circle(window, 'aqua', (coords), (3))
    for i in [coords]:
        distance_from_center = math.hypot(x - 150, y - 150)
        is_in_circle = distance_from_center <= 300 / 2

        if is_in_circle == True:
          red_score +=1
        if is_in_circle == False:
            pygame.draw.circle(window, 'lime', (coords), (5))

    x = random.randrange(0, 300)
    y = random.randrange(0, 300)
    coords = [x, y]

    pygame.draw.circle(window, "blue", (coords), (5))
    for i in [coords]:
        distance_from_center = math.hypot(x - 150, y - 150)
        is_in_circle = distance_from_center <= 300 / 2

        if is_in_circle == True:
          Player_blue_score +=1
        if is_in_circle == False:
            pygame.draw.circle(window, 'orange', (coords), (3))

    pygame.display.flip()
   
print("Blue had", blue_score)
print("Red had", red_score)

if player_selected == "red" and Player_red_score > Player_blue_score: 
  print("Player Red Wins!")
  print("You Win!")
if player_selected == "red" and Player_red_score < Player_blue_score:
  print("Player Blue Wins!")
  print("You Lose!")
if player_selected == "blue" and Player_blue_score > Player_red_score:
  print("Player Blue Wins!")
  print("You Win!")
if player_selected == "blue" and Player_blue_score < Player_red_score:
  print("Player Red Wins!")
  print("You Lose!")
if player_selected == "blue" and Player_blue_score == red_score:
  print("Tie!")
  print("Draw Result")
if player_selected == "red" and Player_red_score == Player_blue_score:
  print("Tie!")
  print("No Winner")

  pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

pygame.display.flip()
       
       



