// Name: Abigail Bui
// Period: 3
// Assignment: Classes
// Time Spent: 4 hours


import java.util.Random;


class D4 {
    int sides;
    Random random = new Random();
    int num;

    public D4(int sides, int num) {
        this.sides = 4;
        this.num = random.nextInt(5);
    }

    public void rollD4() {
        System.out.println("4-sided die:" + this.num);
    }
}


class Main {
    
    public static void main(String[] args) {
        D4 myD4 = new D4(4,5);

        // Accessing fields and invoking methods using dot notation
        myD4.rollD4();
    }
}

