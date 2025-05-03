public class Solution {



    public int searchInsert(int[] nums, int target) {

        int wantedIndex = binarySearch(nums, target);
        
        if(target > nums[wantedIndex] && wantedIndex +1 <= nums.length-1  && target > nums[wantedIndex + 1]){
            return wantedIndex + 2;
        }
        else if (target > nums[wantedIndex]){
            return wantedIndex + 1;
        }
        
        return wantedIndex;
        
    }

    private int binarySearch(int[] nums, int target){

        int begin = 0;
        int end = nums.length - 1; 
        int middle = 0;

        int counter = (int)Math.ceil(Math.log(nums.length-1) / Math.log(2));
        
        for (int i = 0; counter + 1 > i; i++){
            
            middle = (begin+end) / 2;
            
            if(nums[middle] == target){
                return middle;
            }
            else if(nums[middle] < target){
                begin = middle;

            }
            else if (nums[middle] > target){
                end = middle;
            }

        }

        return middle;
    }
}