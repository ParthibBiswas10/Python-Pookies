
n = int(input("Enter the number of cities: "))
cities_list = []  
for i in range(n):
    a = input()  
    cities_list.append(a)  
unique_cities = set(cities_list)
print(len(unique_cities))

