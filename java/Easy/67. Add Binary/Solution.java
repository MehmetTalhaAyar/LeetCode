public class Solution{


    public String addBinary(String a, String b) {
        int count = 0;
        
        if(a.length() > b.length()){
            count = a.length() - b.length();
            b = "0".repeat(count)  + b;
        }else if (b.length() > a.length()){
            count = b.length() - a.length();
            a = "0".repeat(count) +a;
        }

        char[] first = a.toCharArray();
        char[] second = b.toCharArray();
        
        StringBuilder result = new StringBuilder("");
    
        int plusOne = 0;
        for(int i= first.length-1;i >=0;i--){
            int sayi = Character.getNumericValue(first[i]) + Character.getNumericValue(second[i]);
            
            if(sayi + plusOne >= 2){
                
                if(sayi + plusOne == 2)  
                    result.insert(0, '0');
                else
                result.insert(0, '1');
                plusOne = 1;
            }else{
                result.insert(0, plusOne+sayi);
                plusOne = 0;
            }

        }
        

        if( plusOne == 1){
            result.insert(0, '1');
        }

        return result.toString();
    }



}