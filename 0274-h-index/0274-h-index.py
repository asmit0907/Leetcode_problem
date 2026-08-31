class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        max_h = 0
        
        # Test every possible H-index candidate from 0 to n
        for potential_h in range(n + 1):
            count = 0
            
            # Count how many papers have AT LEAST potential_h citations
            for j in range(n):
                if citations[j] >= potential_h:
                    count += 1
            
            # If we found at least potential_h papers, it's a valid H-index
            if count >= potential_h:
                max_h = max(max_h, potential_h)
                
        return max_h
        
        