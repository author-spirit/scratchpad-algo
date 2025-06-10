// https://leetcode.com/problems/check-if-numsay-is-sorted-and-rotated/

import java.util.*;

public class CheckSorted {
    public static void main(String[] args){
        int[] nums = {1,2};

        boolean isSorted = true;
        int i = 0;
        while(i < nums.length-1){
            if(nums[i] < nums[i+1]){
                i++;
            }else{
                isSorted = false;
                break;
            }
        }
    
        System.out.println("Sorted" + isSorted);
    }
}