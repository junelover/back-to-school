""" this code has been a chellange as i done it with reduced amount functions
and used a lot of if and else so i added comments to explain step by step"""

from os import system, name 
from time import sleep 
  
# define our clear function 
def clear(): 
    # on windows
    if name == 'nt': 
        rn = system('cls') 
  
    # on unix, linux, mac
    else: 
        rn = system('clear') 
print('\n\033[01;01;41m check \033[0;01;0m')
clear()
def load ():
  for i in range(0,26,1):
    sleep(0.1)
    a = i * 4
    clear()
    print('\n\033[01;01;41m LOADING CODE \033[0;01;0m',"[","="*i,"]",a,"%")
load()
  
  
# sleep for 2 seconds after printing output 
sleep(2) 
  
# now call function we defined above 
clear()

def intro():
      print("\n\t\t\t\t\t\tcurrency exchange \033[01;01;41mv3.1\033[0;01;0m\n\t\t\t\t\t\t A tool by Maynard\n")
      print("\n\n\n\n\n\n\033[01;01;41m important note:\033[0;01;0m the program may be inaproprate after few weeks or so.\nAs the ammount value in not fixed and my code is not live\n")



code = "1"  
while True:

  intro()
  #getting data from users
  value =float(input("\nEnter the amount :"))
  clear()
  intro()
  print ("\n1)INR 2)GBP 3)USD 4)EUR 5)AED")
  currency1 = str(input("\nEnter your current Currency :"))

  #comparing and storing the first input from the user and assining the value to it  
  if currency1 == "1":
      h_currency = "INR = "
      c_value = value
  
  elif currency1 == "2":
      h_currency = "GBP = "
      c_value = value

  elif currency1 == "3":
      h_currency = "USD = "
      c_value = value

  elif currency1  == "4":
      h_currency = "EUR = "
      c_value = value

  elif currency1 == "5":
      h_currency = "AED = "
      c_value = value

  else :
      print("\n\033[01;01;41m please enter a valied option: '1-5'\033[0;01;0m")
      sleep(3)
      clear()
      load()
      sleep(1)
      clear()
      continue
    

  #easterEgg here when user tries to convert the same currency he has entered
  clear()
  intro()
  print ("\n1)INR 2)GBP 3)USD 4)EUR 5)AED")
  currency2 = input("\nEnter the Currency you want to convert to  :")
  print ("\n")

  if currency2 == currency1:
      clear()
      intro()
      print("\nit's the same you entered :",h_currency,value)
      cnfrm = str(input("\n\n\ndo you want to coniniue? enter 'Y' for yes or  press any other key to close : "))
      if cnfrm =='Y' or cnfrm =='y' or cnfrm =='Yes' or cnfrm =='YES' or  cnfrm =='yes':
        clear()
        load()
        sleep(1)
        clear()
        continue
      else:
        break

  #comparing and converting the user input to required currency
  elif currency2 == "1":
      c_currency = "INR = "

      if currency1 == "2":
        d_value = 94.7949

      elif currency1 == "3":
        d_value = 73.3026

      elif currency1  == "4":
        d_value = 86.1644

      elif currency1 == "5":
        d_value = 19.9603

      else:
        exit("please enter a valied option")

  elif currency2 == "2":
      c_currency = "GBP = "

      if currency1 == "1":
        d_value = 0.0105461

      elif currency1 == "3":
        d_value = 0.773157

      elif currency1  == "4":
        d_value = 0.909217

      elif currency1 == "5":
        d_value = 0.210572

      else:
        exit("please enter a valied option")

  elif currency2 == "3":
      c_currency = "USD = "

      if currency1 == "2":
        d_value = 1.29347

      elif currency1 == "1":
        d_value = 0.0136434

      elif currency1  == "4":
        d_value = 1.17593

      elif currency1 == "5":
       d_value = 0.272294

      else:
        exit("please enter a valied option")

  elif currency2 == "4":
      c_currency = "EUR = "
 
      if currency1 == "2":
        d_value = 1.09984

      elif currency1 == "3":
        d_value = 0.850399

      elif currency1  == "1":
        d_value = 0.0116016

      elif currency1 == "5":
        d_value = 0.231554 

      else:
        exit("please enter a valied option")

  elif currency2 == "5":
      c_currency = "AED = "
  
      if currency1 == "2":
        d_value = 4.74925

      elif currency1 == "3":
        d_value = 3.67250

      elif currency1  == "4":
        d_value = 4.31832

      elif currency1 == "1":
        d_value = 0.0501011

      else:
        exit("please enter a valied option")

  else :
      print("\033[01;01;41m please enter a valied option: '1-5'\033[0;01;0m")
      sleep(3)
      clear()
      load()
      sleep(1)
      clear()

  clear()
  intro()
  print("\n",h_currency,round(c_value,2),"\n",c_currency,round(d_value * value,2),"\n\n\n")

  cnfrm = str(input("do you want to coniniue? enter 'Y' for yes or press any other key to close : "))
  if cnfrm =='Y' or cnfrm =='y' or cnfrm =='Yes' or cnfrm =='YES' or cnfrm =='yes':
      clear()
      load()
      sleep(1)
      clear()
      continue
  else:
      break
