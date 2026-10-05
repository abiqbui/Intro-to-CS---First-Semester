// Name: Abigail Bui
// Period: 3
// Assignment: File Interaction
// Time Spent: 2 days?



import java.util.Scanner;
import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        // Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        Path path = Path.of("note.txt");
        

        System.out.print("Would you like to make a note? (yes or no): ");
        String yon = scanner.nextLine(); 

        try{
            if (yon.equals("yes") ) {
                System.out.print("Note: ");
                String note = scanner.nextLine();

                Files.writeString(path, note);
            }
            

            System.out.print("Would you like to look at your note? (yes or no): ");
            String look = scanner.nextLine();

            if (look.equals("yes") ) {
                String data = Files.readString(path);
                System.out.println(data);
            }
        } catch (IOException e) {
            e.printStackTrace();

        }
        // 5. Close the scanner to free resources
        scanner.close(); 
    }
}
