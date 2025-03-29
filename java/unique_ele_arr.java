
public class unique_ele_arr {
public static void main(String[] args) {
    int[] a = {3,2,1,3,2};
    int c = 0;
    for(int i : a){
        c ^= i;
    }
    System.out.println(c);
}
}