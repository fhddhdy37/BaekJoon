import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] R = new int[T];
        String[] S = new String[T];

        for(int i = 0; i < T; i++){
            R[i] = sc.nextInt();
            S[i] = sc.nextLine();
            
            for(int j = 0; j < S[i].length(); j++){
                System.out.print(String.valueOf(S[i].charAt(j)).repeat(R[i]).trim());
            }
            System.out.println();
        }
    }
}