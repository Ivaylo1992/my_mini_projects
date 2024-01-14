import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')


#generate a password
def generate_password():
    # If yes, ask for length

    password_length = int(input('How long would you like your password to be?: '))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = ''.join(password)
    print(password)

#Ask the user if they want to generate a password
option = input('Do you like to generate a password? (Yes/No): ')

#Print the passowrd
if option == 'Yes':
    generate_password()
    # if the initial answer is no , exit the program
elif option == 'No':
    print('Program ended')
    quit()
else:
    print('Invalid input!')
    quit()
