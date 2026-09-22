// Name: Abigail Bui
// Period: 2
// Assignment: Loops, Conditionals, & Custom Functions
// Time Spent: 15 min?


import java.util.Scanner; // Import the Scanner class


public class Main {
    public static void main(String[] args) {
        // Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        System.out.print("Y or N?");
        String yon = scanner.nextLine(); 

        if (yon.equals("Y") ) {
            int x = 2;
            while (x == 2) {
                System.out.print("Requirements fufilled");
            }
        }
        

        // 5. Close the scanner to free resources
        scanner.close(); 
    }
}
