import random
password=[]


p=(input("Enter Name: "))
list_p=p.split(" ")
age=input("Enter age: ")
password.append(age)
fav=input("Enter numbers: ")
list_fav=fav.split(",")
n=random.choice(list_fav)
password.append(n)
symbols=['@','#','$']
ns=random.choice(symbols)
password.append(ns)
password=password+list_p
random.shuffle(password)
#print(password)
new_pass=""
for i in password:
    new_pass+=i
print(new_pass)


