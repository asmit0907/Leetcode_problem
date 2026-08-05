class Solution {
    public int countNegatives(int[][] grid) {
        int rows=grid.length;
        int count=0;
        int cols=grid[0].length;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]<0){
                    count+=1;
                }
            }
        }
        return count;
    }
}