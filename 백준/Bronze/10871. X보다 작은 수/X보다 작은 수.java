import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();
        int[] NList = new int[N];
        sc.nextLine();

        for(int i = 0; i < N; i++){
            NList[i] = sc.nextInt();
        }
        sc.nextLine();
        for(int i = 0; i < N; i++){
            if(X > NList[i]){
                System.out.printf("%d ", NList[i]);
            }
        }
    }
}