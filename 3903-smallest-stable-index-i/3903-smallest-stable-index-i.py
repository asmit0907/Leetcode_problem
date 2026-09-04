class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            c=max(nums[0:i+1])
            d=min(nums[i:n])

            if(c-d)<=k:
                return i
        return -1        