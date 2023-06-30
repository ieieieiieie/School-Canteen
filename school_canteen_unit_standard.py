#Sequence 1: Greeting to ask the person's name (completed 29/06/2023, written by William McArthur) Version 1
print("Welcome to our school canteen!")

valid = False 
while not valid: 
  name = input("what is your name? ")
  
  if name.isalpha(): 
        valid = True
        print("Kia Ora {}! welcome to the Fraser High School Canteen!".format(name)) 

  else:
      print("we require your name to proceed")

#Sequence 2: Menu, for prompting the customer to get the menu (completed 29/06/2023, written by William McArthur) Version 1 
import time
import sys

time.sleep(1)

valid = False
while not valid:
  print()
  response = input ("would you like to see the menu? ".lower())
  menu = "On the menu today we have the Pie for $4.50 and the Burger for $7.89. {} what would you like to order? (Please enter Burger or Pie) ".format(name)

  if response == "yes" or response == "y":
   valid = True
   time.sleep(1)
   print(menu)
   print()
  
  elif response == "no" or response == "n":
   valid = True
   print("okay, thanks for visiting the Fraser High School Canteen") 
   sys.exit(0)
  
  else:
    print("Sorry {} but you need to say yes or no".format(name))

#Sequence 3: Ordering Food, to order items listed in the menu (completed 29/06/2023, written by William McArthur) Version 1 

  menu_answer = input("Place your order here ".lower())
  
  if menu_answer == "burger":
    valid = True
    print("Thank you {}! Your burger will be ready shortly".format(name))

  elif menu_answer == "pie":
    valid = True
    print("Thank you {}! Your pie will be ready shortly".format(name))

  else:
    print("sorry {} we need to know if you want a pie or burger".format(name))