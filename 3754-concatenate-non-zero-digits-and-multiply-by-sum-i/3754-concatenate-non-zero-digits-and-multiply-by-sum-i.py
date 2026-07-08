class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0
        for ch in str(n):
            if ch != '0':
                digit = int(ch)
                digit_sum += digit
                x = x * 10 + digit 
                
        return x * digit_sum