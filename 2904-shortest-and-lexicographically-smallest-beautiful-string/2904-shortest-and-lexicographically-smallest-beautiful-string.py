class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        c = n + 1       
        res = ""       
        
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]                 
                if sub.count("1") == k:        
                    if j - i + 1 < c:          
                        c = j - i + 1
                        res = sub
                    elif j - i + 1 == c:         
                        if sub < res:
                            res = sub
                            
        return res