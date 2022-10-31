import random

#generating random number by import
number = random.randrange(1,11)

chance = 0
correct_guess = False

for i in range(3):
  
  guess = input("Guess the number: ")
  guess = int(guess)
  chance += 1
  if guess < number:
    print("Too Low.")
  elif guess > number:
    print("Too High.")
  else:  #(guess = number)
    print("Correct!!!")
    print("It took you", chance, "chances to get it correct")
    
    
    
    