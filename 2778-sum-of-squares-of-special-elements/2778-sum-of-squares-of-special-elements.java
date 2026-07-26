class Solution {
    public int sumOfSquares(int[] nums) {
        int n = nums.length; 
        int[] arr = new int[n]; 
        int k = 0; 
        for(int i = 1; i <= n; i++){ 
            if(n % i == 0){ 
                arr[k] = nums[i - 1]; 
                k += 1;
            } 
        } 
        
        int c = 0; 
        for(int i = 0; i < n; i++){ 
            c = c + (arr[i] * arr[i]); 
        } 
        return c; 
    } 
}

//     int n = nums.length;
//         int sum = 0;
        
//         // Loop through the array using 0-based index 'i'
//         for (int i = 0; i < n; i++) {
//             // Convert to 1-based index (i + 1) to check if it divides n
//             if (n % (i + 1) == 0) {
//                 sum += nums[i] * nums[i];
//             }
//         }
        
//         return sum;
//     }
// }
// }