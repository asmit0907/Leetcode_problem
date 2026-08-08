class Solution {
    public int singleNonDuplicate(int[] nums) {
        int n=nums.length;
        int l=0;
        int h=n-1;
        int mid;

        while (l < h) {
            mid = l + (h - l) / 2;
            if (mid % 2 == 1) {
                mid--;
            }
            if (nums[mid] == nums[mid + 1]) {
                l = mid + 2;
            } else {
                h = mid;
            }
        }
        
        return nums[l];
    }
}
    