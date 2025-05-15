import java.util.List;

public class Solution{
    
    private final int MOD = (int) 1e9 + 7;
    private final int LENGTH = 26;

    public int lengthAfterTransformations(String s, int t, List<Integer> nums) {
        
        // Verilen s stringinde hangi karakterden ne kadar oldugunu soyluyor
        int[] characterMatrix = new int[LENGTH];
        for (char ch : s.toCharArray()) {
            characterMatrix[ch - 'a']++;
        }


        // burada her elemanin hangi elemanlara donusecegi teker teker yazdirilir 
        // a harfi icin ilk sutun olmak uzere tum harfler
        int[][] convertMatrix = new int[LENGTH][LENGTH];

        for(int i= 0; i < LENGTH;i++){
            for(int j = 1;j <= nums.get(i);j++){
                convertMatrix[(i+j) % LENGTH][i] = 1;
            }
        }


        
        // Hızlı üs alma için başlangıçta identity (birim) matrisi oluştur
        int[][] result = new int[LENGTH][LENGTH];

        for(int i= 0;i < LENGTH;i++){
            result[i][i] = 1;
        }
   
        // convertMatrix matrisinin t. kuvvetini bul: fast matrix exponentiation
        while (t > 0) {
            if (t % 2 == 1) result = multiply(result, convertMatrix); // t tekse çarp

            convertMatrix = multiply(convertMatrix, convertMatrix); // karesini al
            t /= 2;
        }
        
        

        // Elde edilen dönüşüm sonucunu, başlangıç karakter sayılarıyla çarp ve toplam uzunluğu bul
        int ans = 0;
        for (int i = 0; i < LENGTH; i++) {
            for (int j = 0; j < LENGTH; j++) {
                ans = (int) ((ans + (long) result[i][j] * characterMatrix[j]) % MOD);
            }
        }


        return ans;
    }

    // İki matrisi çarpan ve sonucunu donduren fonksiyon
    public int[][] multiply(int[][] A, int[][] B) {
        int[][] result = new int[LENGTH][LENGTH];

        for (int i = 0; i < LENGTH; i++) {
            for (int j = 0; j < LENGTH; j++) {
                for (int k = 0; k < LENGTH; k++) {
                    result[i][j] = (int) ((result[i][j] + (long) A[i][k] * B[k][j]) % MOD);
                }
            }
        }

        return result;
    }
    

}