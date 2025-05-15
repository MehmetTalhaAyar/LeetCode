import java.util.ArrayList;
import java.util.List;

public class Solution {

    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        List<String> longestSubsequence = new ArrayList<>();


        if(words.length == 1){
            longestSubsequence.add(words[0]);
            return longestSubsequence;
        }

        int counter = 1;
        int lastElement = groups[0];
        longestSubsequence.add(words[0]);
        while(counter < groups.length){
            

            if(lastElement != groups[counter]){
                lastElement = groups[counter];
                longestSubsequence.add(words[counter]);
            }

            counter++;
        }


        return longestSubsequence;
    }

}