import re
from os import path


def create_user_name():
    while True:
        user_in = str(input('Create a username: '))
        if 8 <= len(user_in) <= 12:
            username = open('username.txt', 'w')
            username.write(user_in)
            username.close()
            break
        else:
            print('user Name should be between 8 to 12 characters')
    return username


def create_password():
    while True:
        user_in = str(input('Create password: '))
        if 8 <= len(user_in) <= 12:
            if re.search(r'[A-Z]', user_in):
                if re.search(r'[0-9]', user_in):
                    re_user_in = str(input('Confirm password: '))
                    if re_user_in == user_in:
                        password = open('password.txt', 'w')
                        password.write(user_in)
                        password.close()
                        break
                    else:
                        print('password did not match')
                else:
                    print('password should contain at least one number')
            else:
                print('password should contain both uppercase and lowercase laters.')
        else:
            print('password should be between 8 to 12 characters')
    return password


def login():
    while True:
        if not path.isfile('username.txt'):
            create_user_name()
        if not path.isfile('password.txt'):
            create_password()

        if path.isfile('username.txt') and path.isfile('password.txt'):
            uname = open('username.txt', 'r')
            for u in uname:
                u = u
            uname.close()
            passwd = open('username.txt', 'r')
            for p in passwd:
                p = p
            passwd.close()

            username = str(input('Enter your username: '))
            if username != u:
                print('invalid user')
            else:
                password = str(input('Enter the password: '))
                if p != password:
                    print('Incorrect password')
                else:
                    print('Login completed')
                    break
    return True
