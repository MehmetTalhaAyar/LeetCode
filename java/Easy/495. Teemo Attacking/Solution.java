public class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        
        int poisonedDuration = 0;

        for(int i = 0;i < timeSeries.length-1;i++){

            if(timeSeries[i] + duration > timeSeries[i+1]){
                poisonedDuration += timeSeries[i+1]-timeSeries[i];
            }
            else{
                poisonedDuration += duration;
            }

        }
        poisonedDuration += duration;

        return poisonedDuration;
    }
}
