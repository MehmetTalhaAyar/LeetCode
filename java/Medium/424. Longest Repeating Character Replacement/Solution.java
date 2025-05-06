class Solution {
    public int characterReplacement(String s, int k) {
        
        char[] chars = s.toCharArray();

        if(chars.length == 1)
            return 1;

        
        int maxLetter = 0;
        int increaseNumber = 0;
        int i = 0;

        while(i < chars.length){
            
            int lastIndex = i + 1 + k + increaseNumber;
            if(lastIndex >= chars.length)
                lastIndex = chars.length;


            int letterCount = 0;

            for (int j = i;j < lastIndex;j++) {
                if (chars[j] == chars[i]) {
                    letterCount++;
                }
            }

            if(increaseNumber >= letterCount){
                
                if(maxLetter < k + increaseNumber){
                    if( k + increaseNumber >= chars.length ){
                        maxLetter = chars.length;
                        break;
                    }else if(increaseNumber > chars.length/2){
                        maxLetter = k + increaseNumber;
                        break;
                    }
                    else{
                        maxLetter = k + increaseNumber;
                    }

                }
                i++;
                continue;
            }

            increaseNumber = letterCount;
            
        }
        return maxLetter;
    }

    
}