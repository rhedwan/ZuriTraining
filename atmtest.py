userInput = input('Enter your name: ')
users = ['Tunde','Bayo', 'Ridwan','Laguda','Seide','Dibor','MBO']
defaultPin = ['passtunde','passbayo','passlaguda','passseide','passdibor','passmbo']
if userInput in users:
    password = input('Enter your password: ')
    userId = users.index(userInput)
    if password == defaultPin[userId]:
        print('Welcome %s ' %userInput)
        print("These are the availbale option: \n 1. Withdrwal \n 2. cash  deposit \n 3. complaint")
        selectedOption = int(input('Please select an option: '))
        if selectedOption == 1:
            print('Your selected %d' % selectedOption)
        elif selectedOption == 32:
            print('Your selected %d' % selectedOption)
        elif selectedOption == 3:
            print('Your selected %d' % selectedOption)
        else:
            print('Your selected option is unavailble!')   
    else:
        print('Password is incorrect!')
else:
    print('Your details can\'t be found on our database' )