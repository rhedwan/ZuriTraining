from random import randint
from datetime import datetime
database = {}


def init():
    """
    The master_key and account number respectively[ 'admin':1111111111, 'banker':2222222222, 'accountant':3333333333, 'audit':4444444444 and 'manager':5555555555]
     are does with details on our database by default. They are the only ones that can login straight.
    The customer can create account then login afterwards
    """

    print("Welcome to ThePeople'sBank Plc ATM POINT.")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
    print("The current Date and Time :", dt_string)
    haveAccount = int(input("Do you have account with us: 1(yes) 2(no)\n "))
    if haveAccount == 1:
        masterLogin()
    elif haveAccount == 2:
        print(register())
    else:
        print("You have selected wrong option")
        init()


def masterLogin():
    master_input = input('Enter your master key: ').lower()
    master_details = ['admin', 'banker', 'accountant', 'audit', 'manager']
    default_account_num = [1111111111, 2222222222, 3333333333, 4444444444, 5555555555]
    if master_input in master_details:
        master_account = int(input('Enter your Master account Number: '))
        master_fetch = master_details.index(master_input)
        if master_account == default_account_num[master_fetch]:
            print('Welcome %s ' % master_input)
            masterOperation()
        else:
            print(f"Your account number is invalid. Recheck!!!")
            masterLogin()
    else:
        print(
            f"Opps..{master_input} is not found on our database. Kindly recheck")
        masterLogin()


def masterOperation():
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3)Exit: "))
    if selectedOption == 1:
        depositOperation()
    elif selectedOption == 2:
        withdrawalOperation()
    elif selectedOption == 3:
        print("Thanks for Banking with us.You are logged out already.")
        exit()
    else:
        print("Invalid option selected!!!")
        masterOperation()


def login():
    print("************** login ***************")

    accountNumberFromUser = int(input("What is your account number? "))
    password = input("What is your password? ")

    for accountNumber, userDetails in database.items():
        if (accountNumber == accountNumberFromUser):
            if (userDetails[3] == password):
                bankOperation(userDetails)
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
        accountNumber = generatingAccountNumber()
        database[accountNumber] = [first_name, last_name, email, password]
        print("Your account has been created successfully")
        print(" * " * 15)
        print("Your account number is %d" % accountNumber)
        print("Make sure you keep it safe!.. ")
        print(" *  " * 15)
        login()


def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    selectedOption = int(input(
        "What would you like to do? (1) Deposit (2) Withdrawal (3)Logout (4) Complaint or Enquiry (5) Exit: "))
    if selectedOption == 1:
        depositOperation()
    elif selectedOption == 2:
        withdrawalOperation()
    elif selectedOption == 3:
        logOut()
    elif selectedOption == 4:
        complaint()
    elif selectedOption == 5:
        print("Have a nice day.")
        exit()
    else:
        print("Invalid option selected!!!")
        bankOperation(user)


def withdrawalOperation():
    print("*********** Withdrawal **************")
    active_balance = 100000
    amount = int(input('How much would you like to withdraw? '))
    if amount < active_balance:
        print('Take your cash')
        print(f'You have ${active_balance - amount} left in your bank')
        print("Thanks for banking with us")
    else:
        print(f"You have exceeded your balance or invalid input.\nYour Current Balance is: ${active_balance}")
        withdrawalOperation()
    exit()


def depositOperation():
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


def logOut():
    login()


def generatingAccountNumber():
    return randint(1111111111, 9999999999)


init()
