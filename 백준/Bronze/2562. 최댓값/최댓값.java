import java.util.Arrays;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numList = new int[9];
        int max = 0;

        for(int i = 0; i < numList.length; i++){
            numList[i] = sc.nextInt();
        }

        for(int i = 0; i < numList.length; i++){
            if(numList[i] > max){
                max = numList[i];
            }
        }
        System.out.println(max);

        for(int i = 0; i < numList.length; i++){
            if(numList[i] == max){
                System.out.println(i + 1);
            }
        }
    }
}