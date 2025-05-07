public class Solution{


    public int[] plusOne(int[] digits) {
        
        int plusOne = 0;

        digits[digits.length-1] += 1;

        for(int i = digits.length -1; i >= 0;i--){

            if(digits[i] == 10){
                digits[i] = 0;
                plusOne = 1;
            }else if(digits[i] + plusOne == 10){
                digits[i] = 0;
            }else{
                digits[i] += plusOne;
                plusOne = 0;
            }
        }
        plusOne = 0;

        if(digits[0] == 0){
            plusOne = 1;
            digits = new int[digits.length+1];
            digits[0] = 1;
        }

        return digits;
    }



    
}