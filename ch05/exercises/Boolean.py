
def percentage_to_letter(score=0):
  score = float(score)
  if score >= 90:
     return "A"
  elif(score < 90) and (score >= 80):
     return "B"
  elif(score < 80) and (score >= 70):
     return "C"
  elif(score < 70) and (score >= 60):
     return "D"
  elif(score < 60):
     return "F" 

def is_passing(letter = None):
    if letter == "A":
      return True
    elif letter == "B":
      return True
    elif letter == "C":
      return True
    elif letter == "D":
      return False
    elif letter == "F":
     return False

inputscore = float(input("Enter your exam percentage: "))
result = percentage_to_letter(inputscore)
print(result)

result = is_passing(result)
print(result)





    


  



    


