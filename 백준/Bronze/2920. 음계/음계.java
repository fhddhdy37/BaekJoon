import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] scale = new int[8];
        int countBig = 0;
        int countSmall = 0;

        for(int i = 0; i < 8; i++){
            scale[i] = sc.nextInt();
        }

        for(int i = 1; i < 8; i++){
            if(scale[i] > scale[i - 1]){
                countBig++;
            }
            else if(scale[i] < scale[i - 1]){
                countSmall++;
            }
        }

        if(countBig == 7){
            System.out.println("ascending");
        }
        else if(countSmall == 7){
            System.out.println("descending");
        }
        else{
            System.out.println("mixed");
        }
    }
}