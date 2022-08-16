# Non OOP
# Bank Version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

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
    action= action[0]  # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print('Your balance is:', accountBalance)
    elif action == 'd':
        print('Get Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        if userPassword != accountPassword:
            print('Incorrect password.')
        else:  # ok
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is:', accountBalance)
    elif action == 's':  # show
        print('Show:')
        print('     Name', accountName)
        print('     Balance', accountBalance)
        print('     Password', accountPassword)
        print()
    elif action == 'q':
        break
    elif action == 'w':
        print('Withdraw:')

        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        if userWithdrawAmount < 0:
            print('You can not withdraw a negative amount.')
        elif userPassword != accountPassword:
            print('Incorrect password for this account.')
        elif userWithdrawAmount > accountBalance:
            print('You can not withdraw more than you have in your account.')
        else:  # ok
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is:', accountBalance)
print('Done')
