import operator
import random

#selects a random operator and 2 random integers between 1 and 10
ops = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
x = random.randrange(1,11)
y = random.randrange(1,11)
op = random.choice(list(ops.keys()))

#calculates the randomly created equation
answer = ops.get(op)(x,y)

#asks the user to calculate the previously generated equation
print ("Jy! You a robot?\n" )
print ("What is %d %s %d?\nRound to 2 decimal places" % (x, op, y))
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