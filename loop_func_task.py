from random import randint
from datetime import datetime
database = {
    4521996984: ['Adeyemo', 'Ridwan', 'adesolaridwan2003@gmail.com', 'pass'],
    9118978771: ['Josh', 'Mark', 'thejosh25@gmail.com', 'python'],
    6721992344: ['Endurance', 'Mark', 'mazkthebook2003@yahoo.com', 'the:::the'],
    8521902384: ['Simon', 'Peter', 'ilovetheworld01@gmail.com', 'drowssap'],
    4195992235: ['Faith', 'Kolawole', 'theinterns@hotmail.com', 'loop_func']

}


def init():
    print("Welcome to ThePeople'sBank Plc ATM POINT.")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
    print("The current Date and Time :", dt_string)
    have_account = int(input("Do you have account with us: 1(yes) 2(no)\n "))
    if have_account == 1:
        login()
    elif have_account == 2:
        print(register())
    else:
        print("You have selected wrong option")
        init()


def login():
    print("************** login ***************")

    account_number_from_user = int(input("What is your account number? "))
    password = input("What is your password? ")

    for accountNumber, userDetails in database.items():
        if accountNumber == account_number_from_user:
            if userDetails[3] == password:
                bank_operation(userDetails)
    print("Invalid account or password")
    login()


def register():
    print("********** Register **********")
    email = input("What is your email address: ")
    if ('@gmail.com' or '@yahoo.com' or '@hotmail.com') not in email:
        print("You have provided an invalid email address. Kindly recheck.")
        register()
    else:
        first_name = input("What is your first name: ")
        last_name = input("What is your last name: ")
        password = input("Create a password: ")
        account_number = generating_account_number()
        database[account_number] = [first_name, last_name, email, password]
        print("Your account has been created successfully")
        print(" * " * 15)
        print("Your account number is %d" % account_number)
        print("Make sure you keep it safe!.. ")
        print(" *  " * 15)
        login()


def bank_operation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    selected_option = int(input(
        "What would you like to do? (1) Deposit (2) Withdrawal (3)Logout (4) Complaint or Enquiry (5) Exit: "))
    if selected_option == 1:
        deposit_operation()
    elif selected_option == 2:
        withdrawal_operation()
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        complaint()
    elif selected_option == 5:
        print("Have a nice day. Thanks for banking with us.")
        exit()
    else:
        print("Invalid option selected!!!")
        bank_operation(user)


def withdrawal_operation():
    print("*********** Withdrawal **************")
    active_balance = 100000
    amount = int(input('How much would you like to withdraw? '))
    if amount < active_balance:
        print('Take your cash')
        print(f'You have ${active_balance - amount} left in your bank')
        print("Thanks for banking with us")
        exit()
    else:
        print(f"You have exceeded your balance or invalid input.\nYour Current Balance is: ${active_balance}")
        withdrawal_operation()
    exit()


def deposit_operation():
    print("********Deposit**********")
    balance = 0
    deposit = int(input('How much would you like to deposit? '))
    print('Current balance: $%d ' % (balance + deposit))
    print("Thanks for banking with us")
    exit()


def complaint():
    print("********Complaint**********")
    msg = input('What are the issues? ')
    emails = input('Kindly provide us your email? ')
    print('Your would receive your ticket ID on this email: %s ' % emails)
    print("Thanks for banking with us. Your message as benn sent to our response team..")
    exit()


def logout():
    login()


def generating_account_number():
    return randint(1111111111, 9999999999)


init()
