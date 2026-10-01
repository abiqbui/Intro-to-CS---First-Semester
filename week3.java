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
import java.io.FileWriter;

public class Main {
    public static void main(String[] args) {
        // Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        File notesFile = new File("notes_file.txt");
        

        System.out.print("Would you like to make a note? (yes or no): ");
        String yon = scanner.nextLine(); 

        if (yon.equals("yes") ) {
            System.out.print("Note: ");
            String note = scanner.nextLine();

            FileWriter Writer = new FileWriter("notes_file.txt");

            Writer.write(note);
            Writer.close();
        }
        

        System.out.print("Would you like to look at your note(s)? (yes or no): ");
        String look = scanner.nextLine();

        if (look.equals("yes") ) {
            Scanner Reader = new Scanner(notesFile);
          
            // Traversing File Data
          	while (Reader.hasNextLine()) {
                String data = Reader.nextLine();
                System.out.println(data);
            }
        }

        // 5. Close the scanner to free resources
        scanner.close(); 
    }
}
