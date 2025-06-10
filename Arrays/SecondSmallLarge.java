// https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/

import java.util.*;

public class SecondSmallLarge {
    public static void main(String[] args){
        int[] arr = {12, 35, 1, 10, 34, 1};
        int small = Integer.MAX_VALUE;
        int secondSmall = Integer.MAX_VALUE;

        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i]);
            if(arr[i] < small){
                secondSmall = small;
                small = arr[i];
            }
            if(arr[i] < secondSmall && arr[i]!=small){
                secondSmall = arr[i];
            }
        }

        int large = Integer.MIN_VALUE;
        int secondLarge = Integer.MIN_VALUE;

        for(int i=0;i<arr.length;i++){
            if(arr[i] > large){
                secondLarge = large;
                large = arr[i];
            }
            if(arr[i] > secondLarge && arr[i] != large){
                secondLarge = arr[i];
            }
        }

        System.out.println("Small: " + small);
        System.out.println("2nd: " + secondSmall);

        System.out.println("Large: " + large);
        System.out.println("2nd: " + secondLarge);
    }
}