

#multiplication -loop and accumulator
def multiplication(x , p):
    for i in range(p-1):
      x = x+1
    return x 
# Driven code to check above function
x = 50
p = 4
print(multiplication(x, p))
  
#exponent
def exponent(v,k):
  for i in range(k-1):
    v *= v
  return v
# Driven code to check above function
v = 50
k = 4
print(exponent(v, k))

#square
x = 12
n = 4
sqaure = multiplication(x,n) * multiplication(x,n)
print (sqaure)














