import java.util.Scanner;

    public class try1{

        public static void main(String[] args) {

            Scanner sc  = new Scanner(System.in);
            System.out.print("Enter the value of n: ");
            int n  = sc.nextInt();
            System.out.print("Enter the value of m: ");
            int m = sc.nextInt();
            int dominos = m*n/2;
            System.out.println(dominos);
        }
    }
