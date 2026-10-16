// Name: Abigail Bui
// Period: 2
// Assignment: Input, Output, Variables, & Arrays
// Time Spent: 1 hour


#include <iostream>
using namespace std;

int main() {

    int num1;
    cout << "Input a number: ";
    cin >> num1; 

    int num2;
    cout  << "Input another number: ";
    cin >> num2;

    int method;
    cout << "Ready to do math? (enter 1 for yes): ";
    cin >> method;

    
    int sum = num1+num2;
    cout << num1 << "+" << num2 << "=" << sum << "\n";

        
    int difference = num1-num2;
    cout << num1 << "-" << num2 << "=" << difference << "\n";


    int product = num1*num2;
    cout << num1 << "*" << num2 << "=" << product << "\n";


    int quotient = num1/num2;
    cout << num1 << "/" << num2 << "=" << quotient << "\n";


    int solutions[4] = {sum, difference, product, quotient};
    
    for (int element : solutions) {
        std::cout << element << " ";
    }

    

}