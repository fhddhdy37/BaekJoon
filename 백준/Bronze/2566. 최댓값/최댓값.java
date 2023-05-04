import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[9][9];
        int max = 0;
        int max_x = 0;
        int max_y = 0;

        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                arr[i][j] = sc.nextInt();
            }
        }
        sc.nextLine();

        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(arr[i][j] >= max){
                    max = arr[i][j];
                    max_x = i + 1;
                    max_y = j + 1;
                }
            }
        }

        System.out.println(max);
        System.out.printf("%d %d", max_x, max_y);
    }
}
