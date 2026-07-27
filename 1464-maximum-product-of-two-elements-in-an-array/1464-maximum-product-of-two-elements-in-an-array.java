import java.util.Arrays;
class Solution {
    public int maxProduct(int[] nums) {
        int n=nums.length;
        int max=0;
        // Arrays.sort(nums);
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int c=(nums[j]-1)*(nums[i]-1);
                if(c>max){
                    max=c;
                }
            }
        }
        return max;

    }
}