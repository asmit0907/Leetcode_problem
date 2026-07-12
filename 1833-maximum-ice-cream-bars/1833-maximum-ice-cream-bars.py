class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        coin=coins
        count=0
        for i in range(len(costs)):
            if costs[i] > coin:
                break 
            coin=coin-costs[i]
            count+=1

        return count

        