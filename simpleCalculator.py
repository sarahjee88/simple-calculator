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

selection = int(input("Choice: ")) # make a variable called selection that is equal to inputted integer


def addition (num1, num2): # make a function that adds two numbers
    return num1 + num2 # return the final value

def subtraction (num1, num2): # make a function that subtracts two numbers
    return num1 - num2 # return the final value

def multiplication (num1, num2): # make a function that multiplies two numbers
    return num1 * num2 # return the final value

def division (num1, num2): # make a function that divides numbers
    return num1 / num2 # return the final value

num1 = int(input("Put first number: ")) # make a variable called num1 that is equal to inputted integer
num2 = int(input("Put second number: ")) # make a variable called num2 that is equal to inputted integer

if selection == 1: # if statement that works when the selection is equal to 1
    print "%d + %d = " % (num1, num2), addition(num1, num2) # print formatters and operands with final value
elif selection == 2: # if statement that works when the selection is equal to 2
    print "%d - %d = " % (num1, num2), subtraction(num1, num2) # print formatters and operands with final value
elif selection == 3: # if statement that works when the selection is equal to 3
    print "%d * %d = " % (num1, num2), multiplication(num1, num2) # print formatters and operands with final value
elif selection == 4: # if statement that works when the selection is equal to 4
    print "%d / %d = " % (num1, num2), division(num1, num2) # print formatters and operands with final value
else: # if selection is other than 1, 2, 3, or 4, then operate below lines of code
    print "Invalid input. Please pick another one." # print text
