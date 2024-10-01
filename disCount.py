"""arr=[10,30,40,50,20]
b=0
k=3

for i in range(0,len(arr)):
    minn=float('inf')
    for j in range(i+1,min(i+k+1,len(arr))):
        a=abs(arr[i]-arr[j])
        if minn >a:
            minn=a
    b+=minn

print(b)"""
arr = [10, 30, 40, 50, 20]
b = 0  # To store total minimum cost
k = 3  # Maximum jump distance

for i in range(0, len(arr) - 1):  # Stop before the last stone
    minn = float('inf')  # Reset minimum to a very large value for each stone
    for j in range(i + 1, min(i + k + 1, len(arr))):  # Ensure j doesn't go out of bounds
        a = abs(arr[i] - arr[j])  # Calculate the jump cost
        if minn > a:  # Update minimum cost
            minn = a
    if minn != float('inf'):        
        b += minn  # Add the minimum cost to total cost

print(b)  # Output the total minimum costs
