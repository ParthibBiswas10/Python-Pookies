def is_valid(num):
    # Helper function to check if the number contains the digit '9'
    return '9' not in str(num)

def find_nth_number(n):
    current = 0
    count = 0
    while count < n:
        current += 1
        if is_valid(current):
            count += 1
    return current

# Example usage:
n = int(input("Enter a positive integer n: "))
result = find_nth_number(n)
print(f"The {n}-th natural number after removing numbers with digit 9 is: {result}")
