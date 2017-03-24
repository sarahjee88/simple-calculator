print "Thanks for using my trashy calculator... :)" # print text
print "Please choose an option below:" # print text
print """
\n1. Addition
\n2. Subtraction
\n3. Multiplication
\n4. Division

\n\n *NOTICE*
\nIf you try other number than these four,
\nyou will get an error message at the end...
""" # print multiple lines of text

selection = int(input("Choice: "))


def addition (num1, num2): # make a function that adds two numbers
    return num1 + num2

def subtraction (num1, num2): # make a function that subtracts two numbers
    return num1 - num2

def multiplication (num1, num2): # make a function that multiplies two numbers
    return num1 * num2

def division (num1, num2): # make a function that divides numbers
    return num1 / num2

num1 = int(input("Put first number: "))
num2 = int(input("Put second number: "))

if selection == 1:
    print "%d + %d = " % (num1, num2), addition(num1, num2)
elif selection == 2:
    print "%d - %d = " % (num1, num2), subtraction(num1, num2)
elif selection == 3:
    print "%d * %d = " % (num1, num2), multiplication(num1, num2)
elif selection == 4:
    print "%d / %d = " % (num1, num2), division(num1, num2)
else:
    print "Invalid input. Please pick another one."
