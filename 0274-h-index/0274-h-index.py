class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        max_h = 0
        
        # Test every possible H-index candidate from 0 to n
        for i in range(n + 1):
            count = 0
            
            # Count how many papers have AT LEAST i citations
            for j in range(n):
                if citations[j] >= i:
                    count += 1
            
            # If we found at least i papers, it's a valid H-index
            if count >= i:
                max_h = max(max_h, i)
                
        return max_h
        
        