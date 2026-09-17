// Name: Abigail Bui
// Period: 2
// Assignment: Input, Output, Variables, & Arrays
// Time Spent: 

import java.util.Scanner; // Import the Scanner class
import java.util.ArrayList;  // Import the ArrayList class

public class Main {
    public static void main(String[] args) {
        // Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        int x = 2;
        
        // Create ArrayList object
        ArrayList<String> birthdays = new ArrayList<>();

        while (x == 2) {


            // Prompt the user and read a String
            System.out.print("Enter a birthday: ");
            String bday = scanner.nextLine(); 

            birthdays.add(bday);

            // Output the results
            System.out.println(birthdays);

        }

        // 5. Close the scanner to free resources
        scanner.close(); 
    }
}
