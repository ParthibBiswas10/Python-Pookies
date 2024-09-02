import math
def can_cal(height,width,coverage):
    area=height*width
    can=math.ceil(area/coverage)
    print(f"no of cans needed is {can}")


h=int(input("Enter height: "))
w=int(input("enter width: "))
c=int(input("Enter Coverage: "))
can_cal(h,w,c)