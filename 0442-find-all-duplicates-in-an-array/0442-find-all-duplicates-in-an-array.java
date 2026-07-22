import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
class Solution {
    public List<Integer> findDuplicates(int[] nums) {

        int n = nums.length;
        List<Integer> arr = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                arr.add(nums[i]);
            }
        }
        
        return arr;
        
    }
}
 