def star_pyramid():
  print("number of rows")
  num = int(input(":"))
  
  star = 1
  
  for i in range(num):
    print ("*"*star)
    star = star+1

star_pyramid()

def rstar_pyramid():
  print("number of rows")
  num = int(input(":"))
  
  for i in range(num):
    print("*"*num)
    num = num-1

rstar_pyramid()



