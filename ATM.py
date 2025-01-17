#ATM
def show_balance(balance):
    print("********************************")
    print(f"Your balance is: ${balance:.2f}")
    print("********************************")

def deposit():
    amount = float(input("Please enter deposit amount: "))
    if amount < 0:
        print("The amount must be greater than 0.")
        return 0
    else:
        return amount 

def withdraw(balance):
    amount = float(input("Please enter withdrawal amount: "))
    if amount > balance:
        print("******************")
        print("Insufficient Funds")
        print("******************")
        return 0
    elif amount < 0:
        print("**********************************")
        print("The amount must be greater than 0.")
        print("**********************************")
        return 0
    else:
        return amount

def main():
    balance = 100
    running = True

    while running:
        print("***************************")
        print("  PLEASE SELECT AN OPTION")
        print("***************************")
        print()
        print("1. CHECK BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. EXIT")
        print()

        option = input("OPTION (1-4): ")

        if option == '1':
            show_balance(balance)
        elif option == '2':
            balance += deposit()
        elif option == '3':
            balance -= withdraw(balance)
        elif option == '4':
            running = False
        else:
            print("That is an invalid option.")

    print("THANK YOU! HAVE A GREAT DAY!")

if __name__ == '__main__':
    main()
