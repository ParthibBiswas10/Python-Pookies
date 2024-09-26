#list=[2,3,4,5,6]
list=eval(input("Enter List: "))
print(f"Previous List: {list}")
a=0
for i in list:
    square=i**2
    list[a]=square
    a=a+1
print(f"New List: {list}")