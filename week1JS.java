// Name: Abigail Bui
// Period: 2
// Assignment: Input, Output, Variables, & Arrays
// Time Spent: 

import java.util.Scanner; // 1. Import the Scanner class

public class Main {
    public static void main(String[] args) {
        // 2. Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        // 3. Prompt the user and read a String
        System.out.print("Enter your name: ");
        String name = scanner.nextLine(); 

        // 4. Prompt the user and read an Integer
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        // Output the results
        System.out.println("Hello " + name + "! You are " + age + " years old.");

        // 5. Close the scanner to free resources
        scanner.close(); 
    }