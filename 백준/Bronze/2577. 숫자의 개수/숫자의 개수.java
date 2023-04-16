import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = a * b * c;
        String num = String.valueOf(d);
        int[] n = new int[10];

        for(int i = 0; i < 10; i++){
            n[i] = num.length() - num.replace(String.valueOf(i), "").length();
            System.out.println(n[i]);
        }
    }
}