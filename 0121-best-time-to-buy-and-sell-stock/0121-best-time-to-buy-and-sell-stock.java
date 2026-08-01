class Solution {
    public int maxProfit(int[] prices) {
        int n=prices.length;
        int mp=0;
        int m=prices[0];
        for(int i=0;i<n;i++){
            int c=prices[i]-m;
            mp=Math.max(mp,c);
            m=Math.min(m,prices[i]);
        }
        return mp;
    }
}