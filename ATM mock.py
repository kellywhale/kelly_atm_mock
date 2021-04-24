import random


database = {
    1234567890: ['Kelly', 'Thomas', 'ola@gmail.com', 'pass', 500]
}


def init():
    print('Welcome to bankPHP')

    have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print('You have selected invalid option')
        init()


def login():
    print('======= Login =======')

    account_number_from_user = input('What is your account number? \n')
    password = input('what is your password \n')

    for account_number, user_details in database.items():
        if account_number == int(account_number_from_user):
            if user_details[3] == password:
                bank_operation(user_details)
                exit()

    print('Invalid account or password')
    init()


def register():
    print("======= Register ========")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input('What is your last name? \n')
    password = input('create a password for yourself \n')

    account_number = generating_account_number()

    database[account_number] = [first_name, last_name, email, password, 0]
    print('Your Account has been created')
    print('=== ==== ===== ==== ===')
    print("Your Account Number is: %d " % account_number)
    print('Make sure you keep it safe')
    print('=== ==== ===== ==== ===')
    login()


def bank_operation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    selected_option = int(input(
        "What would you like to do? (1) deposit (2) withdrawal (3) Balance (4) logout (5) exit \n"))

    if selected_option == 1:
        deposit_operation(user)

    elif selected_option == 2:
        withdrawal_operation(user)

    elif selected_option == 3:
        current_balance(user)

    elif selected_option == 4:
        logout(user)

    elif selected_option == 5:
        print('Thanks for Banking with us.')
        exit()

    else:
        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    withdraw_amount = int(input('How much would you like to withdraw \n'))
    if withdraw_amount <= user[4]:
        print('Take your money')
        new_current_balance = user[4] - withdraw_amount
        print('%s %s, your current Account balance is %d' % (user[0], user[1], new_current_balance))
        another_transaction(user)

    if withdraw_amount > user[4]:
        print('Insufficient fund')
        another_transaction(user)


def deposit_operation(user):
    deposit_amount = int(input('how much would you like to deposit \n'))
    new_current_balance = user[4] + deposit_amount
    print('%s %s, your current Account balance is %d' % (user[0], user[1], new_current_balance))
    another_transaction(user)


def current_balance(user):
    print('%s %s, your Account balance is %d' % (user[0], user[1], user[4]))
    another_transaction(user)


def logout(user):
    logout_verification = int(input('Are you sure you want to logout (1) Yes (2) No \n'))
    if logout_verification == 1:
        init()
    if logout_verification == 2:
        bank_operation(user)
    else:
        print('Invalid option selected')


def another_transaction(user):
    print('==============================================')
    ask_for_another_transaction = int(input("Do you want to perform another transaction (1) yes (2) no \n"))
    if ask_for_another_transaction == 1:
        bank_operation(user)

    if ask_for_another_transaction == 2:
        print('Thanks for Banking with us.')
        exit()

    else:
        print('invalid option,try again')
        another_transaction(user)


def generating_account_number():
    print('Generating Account Number')
    return random.randrange(1111111111, 9999999999)


# actual banking system
init()
# generatingAccountNumber()
