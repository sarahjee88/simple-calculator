

print "Thanks for using my trashy calculator..." # print text
print "Please choose an option below:" # print text
print """
\n1. Addition
\n2. Subtraction
\n3. Multiplication
\n4. Division
""" # print multiple lines of text

selection = int(input("Choice: "))

num1 = int(input("Put first number: "))
num2 = int(input("Put second number: "))

def addition (): # make a function that adds two numbers
    numAdd = num1 + num2
    return numAdd

def subtraction (): # make a function that subtracts two numbers
    numSub = num1 - num2
    return numSub

def multiplication (): # make a function that multiplies two numbers
    numMult = num1 * num2
    return numMult

def division (): # make a function that divides numbers
    numDiv = num1 / num2
    return numDiv

if selection == 1:
    addition()
elif selection == 2:
    subtraction()
elif selection == 3:
    multiplication()
elif selection == 4:
    division()
else:
    print "Invalid input. Please pick another one."
