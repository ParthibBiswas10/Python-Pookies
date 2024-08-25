s=input("Enter String: ")
for i in s:
    if(s.count(i)==1):
        break
print("1st Non repeats: ",i)