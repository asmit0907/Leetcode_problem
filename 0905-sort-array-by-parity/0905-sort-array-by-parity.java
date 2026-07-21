class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int n=nums.length;
        int[] arr = new int[n]; 
        int k=0;
        int l=n-1;
        for(int i=0;i<n;i++){
            if(nums[i]%2==0){
                arr[k]=nums[i];
                k+=1;
            }
            else{
                arr[l]=nums[i];
                l-=1;
            }
        }
        return arr;

    }
}