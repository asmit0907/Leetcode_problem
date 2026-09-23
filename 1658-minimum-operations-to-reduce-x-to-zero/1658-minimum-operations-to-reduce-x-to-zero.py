class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        s=sum(nums)
        target=s-x

        if target<0:
            return -1
        if target==0:
            return len(nums)

        m=-1
        c=0
        l=0
        for i in range(len(nums)):
            c+=nums[i]
            while c>target and l<=i:
                c-=nums[l]
                l+=1
            if c==target:
                m=max(m,i-l+1)

        return len(nums)-m if m!=-1 else -1
            
        