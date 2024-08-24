n=input("Enter Password: ")
if(len(n)<6):
    print("Password is Weak")
elif(len(n)>6 and len(n)<12):
    print("Password is Medium")
elif(len(n)>12 and len(n)<15):
    print("Password is Strong")