# Non-OOP Bank
# Version 4
# Any number of accounts - with lists

accountNamesList = []
accountBalancesList = []
accountPasswordsList = []


def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)


def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList

    print('Account', accountNumber)
    print('     Name:', accountNamesList[accountNumber])
    print('     Balance:', accountBalancesList[accountNumber])
    print('     Password:', accountPasswordsList[accountNumber])
    print()


def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password.')
        return None
    return accountBalancesList[accountNumber]


def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    if amountToDeposit < 0:
        print("You can not deposit a negative amount")
        return None
    if password != accountPasswordsList[accountNumber]:
        print("Incorrect password.")
        return None
    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] - amountToDeposit
    return accountBalancesList[accountNumber]


def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    if amountToWithdraw < 0:
        print("You can not withdraw a negative amount")
        return None
    if amountToWithdraw > accountBalancesList[accountNumber]:
        print("You can not withdraw more that balance.")
        return None
    if password != accountPasswordsList[accountNumber]:
        print("Incorrect password.")
        return None
    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] - amountToWithdraw
    return accountBalancesList[accountNumber]


print("Joe's account is accoount number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345, "nuts")

while True:
    print()
    print("Press 'b' to get the balance")
    print("Press 'd' to make a deposit")
    print("Press 'n' to create a new account")
    print("Press 'w' to make a withdraw")
    print("Press 's' to show all accounts")
    print("Press 'q' to quit")
    print()

    action = input("What do you want to do?")
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        print("Get Balance:")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userPassword = input("Please enter your password: ")
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print("Your balance is:", theBalance)
    elif action == 'd':
        print("Make Deposit:")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userPassword = input("Please enter your password: ")
        amountToDeposit = int(input("Please enter deposit: "))
        get_deposit = deposit(userAccountNumber, amountToDeposit, userPassword)
        if get_deposit is not None:
            print("Your balance is:", get_deposit)
    elif action == 'n':
        print("Create new account:")
        name_1 = input("Please enter your name for your account: ")
        password_1 = input("Please enter your password: ")
        balance_1 = 0
        create_new = newAccount(name_1, balance_1, password_1)
        print(create_new)
    elif action == 'w':
        print("Make Withdraw:")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userPassword = input("Please enter password: ")
        amountToWithdraw = int(input("Please enter withdraw amount: "))
        get_withdraw = withdraw(userAccountNumber, amountToWithdraw, userPassword)
        if get_withdraw is not None:
            print("Your balance:", get_withdraw)
    elif action == 's':
        accountNumber = int(input("Please enter account number: "))
        print(show(accountNumber))
    elif action == 'q':
        break




