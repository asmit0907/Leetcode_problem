class Solution {
    public int differenceOfSum(int[] nums) {
        int n = nums.length; 
        int sum1 = 0; 
        int sum2 = 0; 
        
        for(int i = 0; i < n; i++){ 
            sum1 += nums[i]; 
            int temp = nums[i]; 
            while (temp > 0) { 
                sum2 += temp % 10; 
                temp /= 10; 
            } 
        }
        return Math.abs(sum1 - sum2); 
    }
}