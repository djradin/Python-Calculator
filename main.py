# Assigning a placeholder value to variables to define them


num1 = "a"
num2 = "a"
opp = "0"
asw = 0


# Simple intro IDK

print("Hello\n")
print("Please choose an operator to be used for this calculation\n")
print("Keep in mind the valid symbols are +, -, /, and *\n")

# Used to get an operator for the calculator
# This ends the program if an invalid input is detected
while str(opp).isdigit() == True:
    opp = input("Please enter a operator\n")
    if opp == "+":
        print("Addition selected\n")
    elif opp == "-":
        print("Subtraction selected\n")
    elif opp == "*":
        print("Multiplication selected\n")
    elif opp == "/":
        print("Division selected\n")
    else:
        print('No valid option selected, please select another value.\n')
# This section simply asks for a number and checks It's a number
# The code is a bit inefficient, but works
# isalpha checks if the string contains a letter, isdigit does the same to numbers
# Also there is probably a way to put these both into one big while loop
# But I don't know how that stuff works

print("Please choose a value for number one.\n")

while str(num1).isalpha() == True:
    num1 = input("Please choose a number\n")
    if str(num1).isdigit() == True:
        print("You chose the number" +" "+ num1  + ".\n")
    if str(num1).isdigit() == False:
        print("You chose the value" +" " + num1 + " this is not a number, try again.\n")

print("Please choose a value for number two\n")

while str(num2).isalpha() == True:
    num2 = input("Please choose a number\n")
    if str(num2).isdigit() == True:
        print("You chose the number" +" "+ num2  + ".\n")
    if str(num2).isdigit() == False:
        print("You chose the value" +" " + num2 + " this is not a number, try again.\n")


print("Both numbers selected\n")

if opp == "+":
    asw = int(num1) + int(num2)
elif opp == "-":
    asw = int(num1) - int(num2)
elif opp == "*":
    asw = int(num1) * int(num2)
elif opp == '/':
    asw = int(num1) / int(num2)

num1 = str(num1)
num2 = str(num2)
asw = str(asw)

print("[THE ANSWER TO " + num1 + " " + opp + " " + num2 + " IS " + asw + ".]")
print("\n________________________________________ \n")

print("Reload the program to try another calculation")

exit()
