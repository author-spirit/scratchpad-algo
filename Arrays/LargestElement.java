// https://takeuforward.org/data-structure/find-the-largest-element-in-an-array/

import java.util.*;

public class LargestElement {

    public static int getMax(int[] arr, int i, int max){
        if(i >= arr.length) {
            return max;
        }
        if(arr[i] > max){
            max = arr[i];
        } 
        return getMax(arr, i+1, max);
    }

    public static void main(String[] args){
        int[] arr = {2,5,1,3,0};
        int max = getMax(arr, 0, 0);    
        System.out.println(max);
    }
}