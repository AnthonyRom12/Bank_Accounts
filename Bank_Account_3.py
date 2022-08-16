# Non OOP
# Bank_Account Version 3
# Two accounts

account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0


def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password


def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Account 0')
        print('     Name: ', account0Name)
        print('     Balance: ', account0Balance)
        print('     Password: ', account0Password)
        print()
    if account1Name != '':
        print('Account 1')
        print('     Name: ', account1Name)
        print('     Balance: ', account1Balance)
        print('     Password: ', account1Password)
        print()


def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password.')
            return None
        return account0Balance
    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password.')
            return None
        return account1Balance


def deposit(accountNumber, depositAmount, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password.')
            return None
    elif password == account0Password:
        depositAmount = input('Please enter deposit amount: ')
        depositAmount = int(depositAmount)
        account0Balance = depositAmount + account0Balance
        return account0Balance

    if accountNumber == 0:
        if password != account1Password:
            print('Incorrect password.')
            return None
    elif password == account1Password:
        depositAmount = input('Please enter deposit amount: ')
        depositAmount = int(depositAmount)
        account1Balance = depositAmount + account1Balance
        return account1Balance


def withdraw(accountNumber, user_withdraw, password):
    global account0Name, account0Balance, account0Password

    if password != account0Password:
        print('Incorrect password.')
        return None
    elif password == account0Password:
        user_withdraw = input('Please entre withdraw amount: ')
        user_withdraw = int(user_withdraw)
        if user_withdraw < 0:
            print('You can not withdraw a negative amount!')
        elif user_withdraw > account0Balance:
            print('You can not withdraw more that your balance!')
        else:
            account0Balance = account0Balance - user_withdraw
            return account0Balance


def withdraw_1(user_withdraw, password):
    global account1Name, account1Balance, account1Password

    if password != account1Password:
        print('Incorrect password.')
        return None
    elif password == account1Password:
        user_withdraw = input('Please entre withdraw amount: ')
        user_withdraw = int(user_withdraw)
        if user_withdraw < 0:
            print('You can not withdraw a negative amount!')
        elif user_withdraw > account1Balance:
            print('You can not withdraw more that your balance!')
        else:
            account1Balance = account1Balance - user_withdraw
            return account0Balance


newAccount(int(input('Please enter account numer:')), input('Please enter name:'), 100,
           input('Please enter password: '))


def main():
    while True:
        print()
        print('Press "b" to get the balance')
        print('Press "d" to get a deposit')
        print('Press "w" to get a withdrawal')
        print('Press "s" to show the account')
        print('Press "q" to quit')
        print()

        action = input('What do you want to do? ')
        action = action.lower()  # force lowercase
        action = action[0]  # just use first letter
        print()

        if action == "b":
            accountNumber = input('Please enter account number: ')
            userPassword = input('Please enter password: ')
            thebalance = getBalance(accountNumber, userPassword)
            if thebalance is not None:
                print("Your balance is:", thebalance)
        elif action == "d":
            userPassword = input('Please enter password: ')
            userDeposit = input('Please enter deposit: ')
            accountNumber = input('Please enter account number: ')
            userDeposit = deposit(accountNumber, userDeposit, userPassword)
            if userDeposit is not None:
                print("Your balance is:", userDeposit)
        elif action == "s":
            accountNumber = input('Please enter account number: ')
            show()
        elif action == 'q':
            break


print('Done')

if __name__ == '__main__':
    main()
