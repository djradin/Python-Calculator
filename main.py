# Assigning a placeholder value to variables to define them


num1 = "a"
num2 = "a"
opp = "0"
asw = 0
calc = 0
unit = 0
K = "a"
F = "a"
C = "a"

# Simple intro to select a calculator
# Asks the user if they would like to use either numeracy or temperature calculators
# May add more in the future and is easily modifiable to add new types of calculators
# If neither are selected it asks them to type again

print("Hello\n")
print("Please select which type of calculator you would like to use\n")
print("The options are temperature and numeracy calculators\n")

while calc != "T" or calc != "N":
    calc = input("Please type either T or N \n")
    if calc == "T" or calc == "t":
        break
    if calc == "N" or calc == "n":
        break

# Temperature calculator, gives options between Kelvin, Celsius and Fahrenheit
# Unlike the last loop, this one is case sensitive as it is a unit of measurement
# That and the code starts to get cluttered with "+ or" statements when I do that

if calc == "T" or calc == "t":
    print("Temperature calculator selected\n")
    print("Please select a temperature to convert from\n")
    print("The options are Kelvin, Fahrenheit, and Celsius\n")
    while unit != "K" or "F" or "C":
        unit = input("Please select K, F, or C\n")
        if unit == "K":
            print("Kelvin selected\n")
            break
        elif unit == "F":
            print("Fahrenheit selected\n")
            break
        elif unit == "C":
            print("Celsius selected\n")
            break
        else:
            print("No valid input detected, please try again\n")
    print("Please select a temperature value\n")

# If the num1 value contains a letter (which it does by default) it does this loop
# Meaning if someone types "L" or another invalid input, it asks to type again

    while num1.isalpha() == True:
        num1 = input("Please enter a number\n")

    print("You have chosen " + num1 + unit + "\n")

# The bulk of this is reformatting the same calculations three ways to s

    if unit == "K":
        F = 1.8 * (int(num1) - 273.15) + 32
        C = int(num1) - 273.15
        print("The value of " + str(K) + " Kelvin in Fahrenheit is " + str(F) + "F and in Celsius it is " + str(
            C) + "C.\n")
        print("Please restart the program to try another calculation")
        exit()
    elif unit == "F":
        K = (int(num1) - 32) / 1.8 + 273.15
        C = (int(num1) - 32) / 1.8
        print("The value of " + str(F) + " Fahrenheit in Celsius is " + str(C) + "C and in Kelvin it is " + str(
            K) + "K.\n")
        print("Please restart the program to try another calculation")
        exit()
    else:
        K = int(num1) + 273.15
        F = (int(num1) * 1.8) + 32
        print("The value of " + str(C) + " Celsius in Fahrenheit is " + str(F) + "F and in Kelvin it is " + str(
            K) + "K.\n")
        print("Please restart the program to try another calculation")
        exit()

elif calc == "N" or "n":
    print("Numeracy calculator selected\n")
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
            print("You chose the number" + " " + num1 + ".\n")
        if str(num1).isdigit() == False:
            print("You chose the value" + " " + num1 + " this is not a number, try again.\n")

    print("Please choose a value for number two\n")

    while str(num2).isalpha() == True:
        num2 = input("Please choose a number\n")
        if str(num2).isdigit() == True:
            print("You chose the number" + " " + num2 + ".\n")
        if str(num2).isdigit() == False:
            print("You chose the value" + " " + num2 + " this is not a number, try again.\n")

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

else:
    print("Invalid input detected")
    exit()
