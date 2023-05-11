import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[][] arr = new int[N][M];
        int[][] sumArr;
        int K = 0;
        int a, b, x, y = 0;
        int sum = 0;

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        K = sc.nextInt();

        for(int i = 0; i < K; i++){
            a = sc.nextInt();
            b = sc.nextInt();
            x = sc.nextInt();
            y = sc.nextInt();

            for(int n1 = a; n1 <= x; n1++){
                for(int n2 = b; n2 <= y; n2++){
                    sum += arr[n1 - 1][n2 - 1];
                }
            }
            System.out.println(sum);
            sum = 0;
        }
    }
}
