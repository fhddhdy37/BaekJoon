import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        int a_int = Integer.parseInt(a);
        int b_int = Integer.parseInt(b);
        int b1 = Integer.parseInt(String.valueOf(b.charAt(0)));
        int b2 = Integer.parseInt(String.valueOf(b.charAt(1)));
        int b3 = Integer.parseInt(String.valueOf(b.charAt(2)));

        System.out.println(a_int * b3);
        System.out.println(a_int * b2);
        System.out.println(a_int * b1);
        System.out.println(a_int * b_int);

    }
}
