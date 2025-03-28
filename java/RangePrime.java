import java.util.Scanner;

public class RangePrime {
    // Change return type to boolean and make it static
    public static boolean isPrime(int a) {
        if (a < 2) return false; // Numbers < 2 are not prime

        for (int i = 2; i * i <= a; i++) { // Efficient loop up to √a
            if (a % i == 0) {
                return false; // Not prime
            }
        }
        return true; // Prime
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter any number: ");
        int n = sc.nextInt();
        sc.close();

        System.out.println("Prime numbers up to " + n + " are:");
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) { // Now correctly calls static method
                System.out.println(i);
            }
        }
    }
}
