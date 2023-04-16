import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = String.valueOf(sc.nextInt());
        String b = String.valueOf(sc.nextInt());
        int revA = Integer.parseInt(new StringBuilder(a).reverse().toString());
        int revB = Integer.parseInt(new StringBuilder(b).reverse().toString());

        if(revA > revB){
            System.out.println(revA);
        }
        else if(revA < revB){
            System.out.println(revB);
        }
    }
}