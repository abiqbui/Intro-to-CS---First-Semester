// Name: Abigail Bui
// Period: 3
// Assignment: File Interaction
// Time Spent: 

#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;

int main() {

    // Open a file
    ofstream file("file.txt");

    string str;
    cout << "Make a note: ";
    cin >> str;

    // Write the string to the file
    file << str;

    int y; 
    cout << "Do you want to read your note? (Input 1 if yes)";
    cin >> y; 



    return 0;
}