class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)
        k=-1
        for i in range(n//2):
            s[i], s[k] = s[k], s[i]
            k-=1
        """
        Do not return anything, modify s in-place instead.
        """
        