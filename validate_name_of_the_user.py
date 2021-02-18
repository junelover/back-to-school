import re
from time import sleep
from os import system, name


def clear_screen():
    if name == 'nt':
        return system('cls')
    else:
        return system('clear')


class name_check:
    def name(self):
            if not re.search(r'[^a-zA-Z]+', self):
                for characters in range(len(self)):
                    self = self.replace(self[characters], self[characters].lower())
                self = self.replace(self[0], self[0].upper())
                clear_screen()
                return self
            else:
                print('Numbers and special characters are not allowed!')
                sleep(3)
                clear_screen()


firstname = str(input('Enter Your first name: '))
firstname = name_check.name
lastname = str(input('Enter Your first name: '))
lastname = name_check.name
print(f'Your name is: {firstname} {lastname}.')
