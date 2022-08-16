# Non OOP
# Bank Account Version 2
# Single Account

accountName = ''
accountBalance = 0
accountPassword = ''


def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
    global accountName, accountBalance, accountPassword
    print('     Name:', accountName)
    print('     Balance:', accountBalance)
    print('     Password:', accountPassword)
    print()


def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect Password.')
    return accountBalance


def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You can not deposit a negative amount!')
        return None
    if password != accountPassword:
        print('Incorrect Password!')
        return None
    accountBalance = accountBalance + amountToDeposit
    return accountBalance


def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You can not withdraw a negative amount!')
        return None
    if password != accountPassword:
        print('Incorrect Password!')
        return None
    if amountToWithdraw > accountBalance:
        print('You can not withdraw more than you have in your account')
        return None
    accountBalance = accountBalance - amountToWithdraw
    return accountBalance


newAccount("Joe", 100, 'soup')  # create an account

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

    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter your password: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 'w':
        print('Withdraw:')
        userWithdraw = input('Please enter amount to withdraw: ')
        userWithdraw = int(userWithdraw)
        userPassword = input('Please enter the password: ')

        newBalance = withdraw(userWithdraw, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 's':
        print('Your Account:')
        show()
    elif action == 'q':
        break
print('Good bye')


