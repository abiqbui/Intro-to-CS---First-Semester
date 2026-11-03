// Name: Abigail Bui
// Period: 3
// Assignment: Classes
// Time Spent: 2 hours?

// g++ week4.cpp -o my__program

#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class D4 {
    public:
    int randNum;
};

int main() {
    D4 myDice;
    srand(time(0));
    myDice.randNum = (rand() % 4) + 1;
    cout << "You rolled: " << myDice.randNum << "\n";
    return 0;
}