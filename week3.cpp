// Name: Abigail Bui
// Period: 3
// Assignment: File Interaction
// Time Spent: 3 hours?

#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {

    // Open a file
    ofstream file("file.txt");

    string str;
    cout << "Make a note: ";
    cin >> str;

    // Write the string to the file
    file << str;

    file.close();

    
    cout << "Your note says: ";

    // Open the text file for reading
    ifstream f("file.txt");

    // Check if the file was opened successfully
    if (!f.is_open()) {
        cerr << "Error opening the file!";
        return 1;
    }

    string s;

    // Read each line from the file
    while (getline(f, s))
        cout << s << endl;

    // Close the file
    f.close();

    return 0;
    
    
}