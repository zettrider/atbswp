'''
Write a function named collatz() that has one parameter named number . If number
is even, then collatz() should print number // 2 and return this value. If 
number is odd, then collatz() should print and return 3 * number + 1 . 

Then write a program that lets the user type in an integer and that keeps 
calling collatz() on that number until the function returns the value 1 .
'''

def collatz(number):
    
    while number != 1:  # number is neq to 1 so we need to carry on
        
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = (number * 3) + 1
            print(number)
        else:
            print('Error!')

#    print(number)

try:
    print('Give me Input. I need an Integer > 0')
    number = int(input())
    if number > 0:
        collatz(number)
    else:
        print('Input should be an Integer > 0!')
except ValueError:
    print('Input should be an Integer!')
