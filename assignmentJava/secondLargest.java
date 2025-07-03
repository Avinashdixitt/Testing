//Assignment 1
package com.avinashd;

import java.util.Scanner;

public class secondLargest {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter no of element in arr");
        int n=sc.nextInt();
        if(n<2){
            System.out.print("Enter  at least two element");
            throw new RuntimeException("Array should have at least 2 elements");
        }
        int [] avi=new int[n];
        for(int i=0;i<n;i++){
            System.out.print("enter "+(i+1)+"Element of arr :");
            avi[i]=sc.nextInt();

        }
        System.out.print("Second largest element of the array is: "+secondLargest(avi));

    }
    public static int secondLargest(int[] arr){
        int ans=Integer.MIN_VALUE;
        int mx=Integer.MIN_VALUE;
        int n= arr.length;
        for (int i=0;i<n;i++){
            if (mx<arr[i]){
                mx=arr[i];
            }}

        for (int i=0;i<n;i++){
                if ((ans<arr[i])&&(arr[i]!=mx)){
                    ans=arr[i];
                }

        }
        return ans;
    }
}
