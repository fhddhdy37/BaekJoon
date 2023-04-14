import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine().trim();
        String[] b;
        int c;

        if(a.equals("")){
            c = 0;
        }else{
            b = a.split(" ");
            c = b.length;
        }

        System.out.println(c);
    }
}
