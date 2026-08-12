from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Add the current element to the window frequency
            freq[nums[right]] += 1
            
            # Shrink the window from the left if the frequency condition is violated
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
                
            # Keep track of the maximum valid window size found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len