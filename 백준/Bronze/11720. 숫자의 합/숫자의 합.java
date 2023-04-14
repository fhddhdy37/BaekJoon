import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        sc.nextLine();
        String numLine = sc.nextLine();
        char[] numEach = numLine.toCharArray();
        int sum = 0;

        for(int i = 0; i < num; i++){
            sum += Character.getNumericValue(numEach[i]);
        }

        System.out.println(sum);
    }
}