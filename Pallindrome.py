s=input("Enter String: ")
rev=""
for char in s:
    rev=char+rev
print("Reversed String is: ",rev)
if s==rev:
    print("Pallindrom")
else:
        print("Not Pallindrom")