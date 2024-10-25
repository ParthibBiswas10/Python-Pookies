class Solution:
    def alternateSort(self, arr):
        
        arr.sort()
        result = []
        
        
        left, right = 0, len(arr) - 1
        
        
        while left <= right:
            if left == right:
                result.append(arr[left])  
            else:
                result.append(arr[right])  
                result.append(arr[left])   
            right -= 1
            left += 1
        
        return result

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1
