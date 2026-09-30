// Name: Abigail Bui
// Period: 3
// Assignment: File Interaction
// Time Spent: 

/*
ask = input("Would you like to make a note? (yes or no): ")

if ask == 'yes' or ask == 'Yes' or ask == 'YES':
    note = input("Note: ")
    with open("notes.txt", "a") as n:
        n.write(f"{note} \n")

look = input("Would you like to look at your note(s)? (yes or no): ")

if look == 'yes' or look == 'Yes' or look == 'YES':
    with open("notes.txt", "r") as n:
        for line in n:
            print(line)
*/

import java.util.Scanner;
import java.io.File;

public class Main {
    public static void main(String[] args) {
        // Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        File obj = new File("myfile.txt");
        

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
