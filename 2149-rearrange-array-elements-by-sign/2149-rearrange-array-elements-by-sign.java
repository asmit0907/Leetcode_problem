class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n=nums.length;
        int k=0;
        int l=1;
        int[] arr1 = new int[n];
        for(int i=0;i<n;i++){
            if(nums[i]>0){
                arr1[k]=nums[i];
                k+=2;
            }
            else{
                arr1[l]=nums[i];
                l+=2;
            }
        }
        return arr1;
    }
}