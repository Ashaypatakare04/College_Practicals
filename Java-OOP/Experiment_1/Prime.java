public class Prime {
    public static void main(String[] arg){
        int a=11;
        if (a>1){
            for(int i=2;i<=a/2;i++){
                if(a%i==0){
                    System.out.println("Not a prime number");
                    return;
                }
            }
            System.out.println("Prime number");
        } else {
            System.out.println("Not a prime number");
        }
    }}
    

