class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_counts = {}
        max_length = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            char_counts[char] = char_counts.get(char, 0) + 1
            while char_counts[char] > 2:
                left_char = s[left]
                char_counts[left_char] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            
        return max_length
        