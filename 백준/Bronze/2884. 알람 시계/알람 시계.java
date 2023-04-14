import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();
        int h = H;
        int m = 0;

        if((H >= 0 && H <= 23) && (M >= 0 && M <= 59)){
            m = M - 45;
            if(m < 0){
                h = H - 1;
                m = 60 + m;
                if(h < 0){
                    h = 24 + h;
                }
            }

            System.out.printf("%d %d\n", h, m);
        }
    }
}