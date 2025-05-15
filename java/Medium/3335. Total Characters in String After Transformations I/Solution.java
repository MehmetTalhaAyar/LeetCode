


public class Solution{
    
    private final int LENGTH = 26;

    private final int MOD = (int) 1e9 + 7;

    public int lengthAfterTransformations(String s, int t) {
        
        int[] characterIndex = new int[LENGTH];

        for(char ch : s.toCharArray()){
            characterIndex[ch - 'a']++;
        }


        for(int i = 0; i < t;i++){

            int[] newArray = new int[LENGTH];
            for(int j = 0; j < LENGTH;j++){
                
                if(j == LENGTH-1){
                    newArray[0] = (newArray[0]+ characterIndex[j]) % MOD; 
                    newArray[1] = (newArray[1]+ characterIndex[j]) % MOD; 
                }else{
                    newArray[(j+1) % LENGTH] = characterIndex[j] % MOD;
                }
                
            }
            characterIndex = newArray;
        }

        int ans= 0;
        for(int i=0;i < LENGTH;i++){

            ans = (ans + characterIndex[i]) % MOD;
        }

        

        return ans;
    }




}