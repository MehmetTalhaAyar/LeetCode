import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {

        int maxResult = 0;
        Map<String,Integer> frequency = new HashMap<>();

        


        for(int i=0 ; i < dominoes.length;i++){

            String key;
            if(dominoes[i][0] > dominoes[i][1]){
                key = String.valueOf(dominoes[i][0]) + String.valueOf(dominoes[i][1]);
            }else{
                key = String.valueOf(dominoes[i][1]) + String.valueOf(dominoes[i][0]);
            }

             

            if(frequency.containsKey(key)){
                frequency.put(key, frequency.get(key).intValue()+1); 
            }else {
                frequency.put(key, 1);
            }

            

        }

        for(String mapKey : frequency.keySet()){


            if(frequency.get(mapKey).intValue() != 1){

                int value = frequency.get(mapKey).intValue();

                maxResult += ( value * (value - 1) / 2);

            }

        }
        return maxResult;
    }


    
}
