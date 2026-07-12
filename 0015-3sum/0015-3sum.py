class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            seen = set()
            j = i + 1
            while j < n:
                complement = -(nums[i] + nums[j])
                
                if complement in seen:
                    res.append([nums[i], complement, nums[j]])
                    
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                        
                seen.add(nums[j])
                j += 1
                
        return res