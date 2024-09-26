import random
l=[0,1,2]
turn=random.choice(l)
if turn==0:
    print("Rock!")
elif turn==1:
    print("Scissor")
elif turn==2:
    print("Paper")