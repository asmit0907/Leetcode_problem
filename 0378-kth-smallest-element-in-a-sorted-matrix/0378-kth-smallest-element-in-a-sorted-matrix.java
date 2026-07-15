class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int row=matrix.length;
        int col=matrix[0].length;
        int[] arr = Arrays.stream(matrix).flatMapToInt(Arrays::stream).toArray(); 
        Arrays.sort(arr); 
        return arr[k-1];
    }
}