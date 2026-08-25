class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        for i in range(1, len(nums) + 2):
            if k * i not in nums_set:
                return k * i