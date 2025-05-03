public class SearchInsertPosition {
    
    public static void main(String arg[]){
        Solution solution = new Solution();

       System.out.println(solution.searchInsert(new int[]{1,3,5,6}, 5) + " expected : 2" );
       System.out.println(solution.searchInsert(new int[]{1,3,5,6}, 2) + " expected : 1" );
       System.out.println(solution.searchInsert(new int[]{1,3,5,6}, 7) + " expected : 4" );
       System.out.println(solution.searchInsert(new int[]{1,3,5,6}, 0)+ " expected : 0" );
       System.out.println(solution.searchInsert(new int[]{1}, 0) + " expected : 0" );
       System.out.println(solution.searchInsert(new int[]{1}, 2) + " expected : 1" );
    }
}
