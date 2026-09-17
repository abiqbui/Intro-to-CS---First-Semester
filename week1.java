// Name: Abigail Bui
// Period: 2
// Assignment: Input, Output, Variables, & Arrays
// Time Spent: 

import java.util.Scanner; // 1. Import the Scanner class
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // 2. Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        int x = 3;
        
        ArrayList<String> birthdays = new ArrayList<>();

        while (x == 2) {


            // 3. Prompt the user and read a String
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
