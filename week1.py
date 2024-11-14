# QUESTION: Basic Calculator Program

# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

# getting the users input
number1 = float(input("Enter a number:"))  #using float notation bcos it takes both decimal and whole number
number2 = float(input("Enter a number:"))
mathOperation = input("Add a mathematucal operation (+,-,*,/):")

#Perfroming the operation based on the user's input and printing the result using if elif expression

if mathOperation == "+":
   result = number1 + number2
   print(f"{number1} + {number2} = {result}")
elif mathOperation == "*":
   result = number1 * number2
   print(f"{number1} * {number2} = {result}")
elif mathOperation == "-":
   result = number1 - number2
   print(f"{number1} - {number2} = {result}")
elif mathOperation == "/":
   if number2 !=0:
      result = number1 / number2
      print(f"{number1} / {number2} = {result}")
   else: 
      print("Error, invalid mathematical operator, enter(+,-,*,/).")
else:
   print("Error, Diving by zero is not supported.")
