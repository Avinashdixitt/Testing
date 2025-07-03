//Assignment 1

package avi;

import java.util.Scanner;

public class StringCheck {
    public static void main(String[] args){
        String s;
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the string for checking wetther it have a,e,i,o,u or not: ");
        s=sc.nextLine();
        System.out.print("Your Testing ans is: "+stringCheck(s));
    }
    public static boolean stringCheck(String str ){
        str=str.toLowerCase();
        return str.contains("a")&&str.contains("e")&&str.contains("i")&&str.contains("o")&&str.contains("u");

    }
}
