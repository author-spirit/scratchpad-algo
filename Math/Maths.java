import java.lang.Math.*;
import java.util.Random;

public class Maths {
    public static void main(String[] args){
        try{
            System.out.println(10/0);
        }catch(ArithmeticException ae){
            System.out.println(ae.getMessage());
        }

        double zero = 0.0;  
        double d = 1.0/zero;  
        
        System.out.println(new Random().nextInt(10));
        System.out.println(Math.min(78, 19));
    }
}