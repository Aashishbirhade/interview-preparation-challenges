public class pattrn {
    public static void main(String[] args) {
        int a = 6;
        for (int i = 1; i <= a; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print('*');  
            }
            System.out.println();  
        }
    }
}
