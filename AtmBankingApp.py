import random

print("\nWelcome to DaInvinc Bank, for your comfort and security")


class Account:
    # Building Account objects
    def __init__(self, id=4545, balance=0):
        self.id = id
        self.balance = balance

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


def main():
    # Creating accounts
    accounts = []

    for i in range(1000, 1050):
        account = Account(i, 0)
        accounts.append(account)

    # ATM Processes
    accountObj = accounts[0]
    while True:
        # Reading id from user
        id = int(input("\nPlease enter account pin: "))

        # Loop till id is valid
        while id != 4545:

            id = int(input("\nInvalid Id.. Re-enter correct pin: "))

        # Iterating over account session
        while True:
            # Printing menu
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")

    # Transaction selection
            selection = int(input("\nPlease enter your selection: "))

    # Getting account object
            for acc in accounts:
                # Comparing account id
                if acc.getId() == id:
                    accountObj = acc
                    break

        # Account Balance
            if selection == 1:
                # Printing balance
                print(accountObj.getBalance(0))

        # Performing Withdrawal
            elif selection == 2:

                # Enter amount
                amt = float(input("\nPlease enter amount to withdraw: "))

        # Verify amount to withdraw
                verify_withdrawal = input(
                    "Please confirm withrawal amount, Yes or No? " + str(amt) + " ")
                if verify_withdrawal == "Yes":
                    print("Verify withdrawal")
                else:
                    break
                if amt <= accountObj.getBalance():

                    # proceed to withdrawal
                    accountObj.withdraw(amt)
                    # print updated balance
                    print("\nUpdated balance: " +
                          str(accountObj.getBalance()) + " n")
                else:
                    print("\nYou have insufficient fund for this withdrawal: " +
                          str(accountObj.getBalance()) + " n")
                    print("\nKindly make a deposit.")
        # Deposit option
            elif selection == 3:
                # enter deposit amount
                amt = float(input("\nPlease enter amount to deposit: "))

        # confirm deposit
                conf_deposit = input(
                    "Please confirm deposit amount, Yes or No ? " + str(amt) + " ")

                if conf_deposit == "Yes":
                    # deposit amount
                    accountObj.deposit(amt)

                    # print updated balance
                    print("\nYour current balance: " +
                          str(accountObj.getBalance()) + " n")
                else:
                    break

        # Exit option
            elif selection == 4:
                print("nTransaction is now complete.")
                print("Transaction number: ",
                      random.randint(10000, 1000000))
                print("Thanks for banking with us")
                exit()

            else:
                print("\nInvalid transaction")


# print("BANK APPLICATION")
# main function
main()
