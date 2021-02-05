class BankAccount {
    int account_no;
    String name;
    int balance;

    BankAccount(int account_no, String name, int balance) {
        this.account_no = account_no;
        this.name = name;
        this.balance = balance;
        System.out.println("Bank Account registered");
    }

    void display() {
        System.out.println("Account Number: " + this.account_no);
        System.out.println("Name: " + this.name);
        System.out.println("Balance: " + this.balance);
    }

    void compare(BankAccount second) {
        if (this.balance > second.balance) {
            System.out.println(this.name + " has more balance than " + second.name);
        } else if (this.balance == second.balance) {
            System.out.println("Both has equal balance");
        } else {
            System.out.println(this.name + " has less balance than " + second.name);
        }
    }

    public static void main(String[] args) {
        BankAccount acc1 = new BankAccount(12234, "Satyam", 15000);
        BankAccount acc2 = new BankAccount(12234, "Raj", 16000);
        acc1.display();
        acc2.display();
        acc1.compare(acc2);
    }
}
