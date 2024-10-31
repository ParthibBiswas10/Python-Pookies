class Solution:
    def countPairsWithDiffK(self, arr, k):
        # Use a set to store elements and a counter for valid pairs
        elements = set(arr)
        count = 0

        # Iterate over each element in the array
        for num in arr:
            # Check if there's a complement that makes the difference k
            if num + k in elements:
                count += 1
            if num - k in elements:
                count += 1
            
            # Remove the number from the set to avoid counting pairs multiple times
            elements.remove(num)
        
        return count

# Driver Code
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1
