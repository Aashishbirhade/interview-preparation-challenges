public class palindrome_str {
    public static void main(String[] args) {
        String a = "dac";
        int i = 0;
        int j = a.length()-1;
        while (i<= j) {
            if (a.charAt(i)!= a.charAt(j)) {
                System.out.println("not palindrom");
                return;
                
            }
            i++;
            j--;  
        }
        System.out.println("is palindrom");
    }
}
