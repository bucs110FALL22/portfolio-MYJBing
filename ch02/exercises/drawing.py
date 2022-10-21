import turtle


myturtle=turtle.Turtle()
drawing_area = turtle.Screen()

myturtle.color('red')


side=int(input("Enter the number of sides "))
length=int(input("Length of each side "))
angle= 360/side

for i in range(side):
  for i in length(length):
    myturtle.fd(length)
    myturtle.rt(angle)
  



drawing_area.exitonclick()