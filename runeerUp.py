if __name__ == '__main__':
    n = int(input("Enter no of scores: "))
    arr = list(map(int, input().split()))
    new_arr=set(arr)
    sorted_arr=sorted(new_arr,reverse=True)
    print(sorted_arr[1])
    