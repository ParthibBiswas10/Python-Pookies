str="Lionel Messi is an Argentina Footballler...born on 24th June 1987"
list=str.split(" ")
print(list)
ab=[word.capitalize() for word in list]
s=" ".join(ab)
print(s)