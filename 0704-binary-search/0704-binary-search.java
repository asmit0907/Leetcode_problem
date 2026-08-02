class Solution {
    public int search(int[] nums, int target) {
        int n=nums.length;
        int h=n-1;
        int l=0;
        int mid;
        while(l<=h){
            mid=(l+h)/ 2;
            if(nums[mid]==target){
                return mid;
            }

            else if(nums[mid]<target){
                l=mid+1;
            }
            else if(nums[mid]>target){
                h=mid-1;
            }
        }
        return -1;

    }
}