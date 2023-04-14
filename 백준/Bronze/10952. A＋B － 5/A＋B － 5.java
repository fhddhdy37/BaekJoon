import java.util.ArrayList;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] num = new String[2];
        ArrayList<Integer> result = new ArrayList<>();
        int a = 0;
        int b = 0;

        while(true) {
            num = sc.nextLine().split(" ");
            a = Integer.parseInt(num[0]);
            b = Integer.parseInt(num[1]);

            if (a == 0 && b == 0) {
                break;
            } else {
                result.add(a + b);
            }
        }

        for(int i: result){
            System.out.println(i);
        }
    }
}