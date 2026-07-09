class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * (n + 2)
        arr[0] = -1         
        k = 1
        count = 1           
        
        for i in range(n):
            if nums[i] == 0:
                arr[k] = i
                k += 1
                count += 1
                
        arr[k] = n         
        count += 1         
        
        l = 0
        for i in range(count - 1):
            j = arr[i+1] - arr[i] - 1
            if j > l:
                l = j

        return l