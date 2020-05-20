import turtle
import time
import random

start = time.time()

#init
t=turtle.Turtle()
t.hideturtle()

# number of points
n = random.randrange(3,10) # number of points
RT = random.randrange(1,200) # deg right turn
L = random.randrange(10,100) # line length
dL = random.randrange(10,100)
LT = RT-360/n

#print parameters
print('n={}'.format(n))
print('RT={}'.format(RT))
print('L={}'.format(L))
print('DL={}'.format(dL))
print('LT={}'.format(LT))


#draw square
for i in range(n):
    t.forward(L-dL/2)
    t.right(RT)
    t.forward(L+dL/2)
    t.left(LT)

stop=time.time()

elapsed = stop-start
#print(elapsed)

time_obj = time.gmtime(elapsed)
date_str = time.strftime("%H:%M:%S", time_obj)
print(date_str)
#keep window open
turtle.done()
