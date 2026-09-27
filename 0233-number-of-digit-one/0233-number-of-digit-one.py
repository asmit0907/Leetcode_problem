
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        
        count = 0
        factor = 1
        
        while factor <= n:
            # Split the number into higher digits, current digit, and lower digits
            higher = n // (factor * 10)
            current = (n // factor) % 10
            lower = n % factor
            
            # 1. Contribution from the higher digits completing full cycles
            count += higher * factor
            
            # 2. Contribution from the current digit depending on its value
            if current == 1:
                count += lower + 1
            elif current > 1:
                count += factor
                
            # Move to the next higher place value (units -> tens -> hundreds...)
            factor *= 10
            
        return count
