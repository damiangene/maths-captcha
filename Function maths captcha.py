import random

def add(a,b):
  return a + b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def truediv(a,b):
  return a/b

#Gives cancer when you dont know how while loops work, also returns a random number between 1 and the argument
def randomer(a):
  fill = random.random()
  fill = int(fill*a)
  while fill == 0:
    fill = random.random()
    fill = int(fill*a)
   
  return fill

i = randomer(4)

if i == 1:
  op = add
  op2 = "+"
elif i == 2:
  op = sub
  op2 = "-"
elif i == 3:
  op = mul
  op2 = "*"
elif i == 4:
  op = truediv
  op2 = "/"

#used randomer here because I dont want to accidentally divide by 0
x = random.random()
x = int(x*10)
y = randomer(10)

#calculates the randomly created equation
answer = op(x,y)

#asks the user to calculate the previously generated equation
print ("Jy! You a robot?\n" )
print ("What is %d %s %d?\nRound to 2 decimal places" % (x, op2, y))
#print "%.2f" % round(answer,2)

#rounds the users input to 2 decimal places so that the upcoming if function can accurately check it
user_ans = float(input(""))
user_ans = round(user_ans,2)
#print user_ans

#checks the users answer with the correct answer
if user_ans == answer:
  print ("Awe, you not a bot.")

else:
  print ("Tsek bot!!!")