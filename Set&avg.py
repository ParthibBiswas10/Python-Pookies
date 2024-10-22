def average(array):
    new=set(array)
    total=sum(new)
    return total/len(new)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)