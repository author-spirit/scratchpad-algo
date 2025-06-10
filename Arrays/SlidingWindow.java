import java.util.*;

public class SlidingWindow {

    public static void maxSubArray(){
        int[] arr = { 5, 8, 2, 1, 8, 7, 9, 11 };
        int k = 4; // Window size
        int maxNum = 0;
        int sum = 0;

        // First Get the sum of k-window
        for(int i=0;i<k;i++){
            sum += arr[i];
        }
        for (int i = k; i < arr.length; i++) {
            sum = sum + arr[k] - arr[i-k];
            maxNum = Math.max(maxNum, sum); 
        }
        System.out.println(maxNum);
    }

    public static void minSubArray(){
        int[] arr = {2, 3, 1, 2, 4, 3};
        int target = 7;

        // window is unknown
        int win = Integer.MAX_VALUE;

        int sum = 0, left = 0;
        // Reduce the initial value and increment the left
        for(int right = 0; right < arr.length; right++){
            sum += arr[right]; // expand

            // If greater than target then shrink the window
            // Remove the leftmost element from sum
            // Shrink until the sum is adjusted
            while(sum >= target){

                // shrink just like in Gamification
                // example: 5-4+1 = 2 i.e [2,3]
                win = Math.min(win, right - left + 1); 
                System.out.println("min: "+ right + " - " + left);
                sum = sum - arr[left];
                left++;
            }
        }

        System.out.println("Minium Window: " + win);

    }

    public static void main(String[] args) {
       minSubArray();
    }
}