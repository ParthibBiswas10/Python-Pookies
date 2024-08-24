numbers=[1,2,3,-5,10,-8,-4,-7,-158,-180,120]
count=0
for i in numbers:
    if i>0:
        count+=1

print("Numbers of +ve numbers: ",count)