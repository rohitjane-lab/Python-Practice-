
class Student:

    def __init__(self,name, marks):
        self.name = name
        self.marks=marks
        self.math =marks[0]
        self.physics =marks[1]
        self.sciencs =marks[2]
    
    def average(self):
        return(self.math + self.physics + self.sciencs)/3
        

s1 =Student("Rohit",[99,20,44])
print(s1.average())
print(s1.name,s1.marks)



class Stu:
    def __init__(self,name,marks):
        self.name  = name 
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hear the all values are add :{sum} The total average is ={sum/3}")

s1=Stu("ROHIT",[99,99,35])
s1.get_avg()
print(s1.name,s1.marks)

class Account:
    user = input("TYPE YOUR PASSWORD",)
    def __init__(self,balance,account_no):
        self.bal = balance
        self.acc_no = account_no
        def __init__(self, password):
            self.pas= password












class ATM:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        return self.balance


def main():
    print("=== ATM Machine ===")
    owner = input("Enter account holder name: ").strip() or "Guest"
    initial_balance = 0.0

    starting_amount = input("Enter opening balance (or press Enter for 0): ").strip()
    if starting_amount:
        try:
            initial_balance = float(starting_amount)
        except ValueError:
            print("Invalid number entered. Starting balance set to 0.")

    account = ATMAccount(owner, initial_balance)
    print(f"Hello, {account.owner}! Your current balance is {account.get_balance():.2f}\n")

    while True:
        print("Choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print(f"Deposit successful. New balance: {account.get_balance():.2f}\n")
            except ValueError as error:
                print(f"Error: {error}\n")
        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                print(f"Withdrawal successful. Remaining balance: {account.get_balance():.2f}\n")
            except ValueError as error:
                print(f"Error: {error}\n")
        elif choice == "3":
            print(f"Current balance: {account.get_balance():.2f}\n")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()


#i=    0        1       2   
a = [[1,2,3],[4,5,6],[7,8,9]]
#j  = 0 1 2   0 1 2   0 1 2 

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[j])