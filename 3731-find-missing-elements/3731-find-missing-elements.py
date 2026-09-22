class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = []
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i+1]:
                for missing_num in range(nums[i] + 1, nums[i+1]):
                    missing.append(missing_num)
                    
        return missing