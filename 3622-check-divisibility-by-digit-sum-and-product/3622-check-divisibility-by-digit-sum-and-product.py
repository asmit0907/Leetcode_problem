class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        c=0
        b=n
        product=1
        while(n!=0):
            c=int(n%10)
            sum+=c
            product*=c
            n=n//10     
        
        return b%(sum+product)==0
