class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr1=[0]*(len(gain)+1)
        
        for i in range(len(gain)):
            arr1[i+1]=arr1[i]+gain[i]

        return max(arr1)
        